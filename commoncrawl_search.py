#!/usr/bin/env python3
"""
Common Crawl URL Search & Page Retrieval

Searches Common Crawl index for URLs matching a pattern and downloads page content.

Usage:
    pip install requests warcio
    python commoncrawl_search.py "https://li.st/Bourdain*" -c CC-MAIN-2018-09 --download
    python commoncrawl_search.py "https://li.st/Bourdain*" --all --download
"""

import argparse
import json
import os
import re
import sys
import time
from urllib.parse import urlparse

import requests
from warcio.archiveiterator import ArchiveIterator

CC_S3_BASE = "https://data.commoncrawl.org/"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0"

# Retry config: 1s, 2s, 4s, 8s, 16s
MAX_RETRIES = 5
INITIAL_BACKOFF = 1

# All available crawl indices (2008-2025)
CRAWL_INDICES = [
    "CC-MAIN-2025-47", "CC-MAIN-2025-43", "CC-MAIN-2025-38", "CC-MAIN-2025-33",
    "CC-MAIN-2025-30", "CC-MAIN-2025-26", "CC-MAIN-2025-21", "CC-MAIN-2025-18",
    "CC-MAIN-2025-13", "CC-MAIN-2025-08", "CC-MAIN-2025-05", "CC-MAIN-2024-51",
    "CC-MAIN-2024-46", "CC-MAIN-2024-42", "CC-MAIN-2024-38", "CC-MAIN-2024-33",
    "CC-MAIN-2024-30", "CC-MAIN-2024-26", "CC-MAIN-2024-22", "CC-MAIN-2024-18",
    "CC-MAIN-2024-10", "CC-MAIN-2023-50", "CC-MAIN-2023-40", "CC-MAIN-2023-23",
    "CC-MAIN-2023-14", "CC-MAIN-2023-06", "CC-MAIN-2022-49", "CC-MAIN-2022-40",
    "CC-MAIN-2022-33", "CC-MAIN-2022-27", "CC-MAIN-2022-21", "CC-MAIN-2022-05",
    "CC-MAIN-2021-49", "CC-MAIN-2021-43", "CC-MAIN-2021-39", "CC-MAIN-2021-31",
    "CC-MAIN-2021-25", "CC-MAIN-2021-21", "CC-MAIN-2021-17", "CC-MAIN-2021-10",
    "CC-MAIN-2021-04", "CC-MAIN-2020-50", "CC-MAIN-2020-45", "CC-MAIN-2020-40",
    "CC-MAIN-2020-34", "CC-MAIN-2020-29", "CC-MAIN-2020-24", "CC-MAIN-2020-16",
    "CC-MAIN-2020-10", "CC-MAIN-2020-05", "CC-MAIN-2019-51", "CC-MAIN-2019-47",
    "CC-MAIN-2019-43", "CC-MAIN-2019-39", "CC-MAIN-2019-35", "CC-MAIN-2019-30",
    "CC-MAIN-2019-26", "CC-MAIN-2019-22", "CC-MAIN-2019-18", "CC-MAIN-2019-13",
    "CC-MAIN-2019-09", "CC-MAIN-2019-04", "CC-MAIN-2018-51", "CC-MAIN-2018-47",
    "CC-MAIN-2018-43", "CC-MAIN-2018-39", "CC-MAIN-2018-34", "CC-MAIN-2018-30",
    "CC-MAIN-2018-26", "CC-MAIN-2018-22", "CC-MAIN-2018-17", "CC-MAIN-2018-13",
    "CC-MAIN-2018-09", "CC-MAIN-2018-05", "CC-MAIN-2017-51", "CC-MAIN-2017-47",
    "CC-MAIN-2017-43", "CC-MAIN-2017-39", "CC-MAIN-2017-34", "CC-MAIN-2017-30",
    "CC-MAIN-2017-26", "CC-MAIN-2017-22", "CC-MAIN-2017-17", "CC-MAIN-2017-13",
    "CC-MAIN-2017-09", "CC-MAIN-2017-04", "CC-MAIN-2016-50", "CC-MAIN-2016-44",
    "CC-MAIN-2016-40", "CC-MAIN-2016-36", "CC-MAIN-2016-30", "CC-MAIN-2016-26",
    "CC-MAIN-2016-22", "CC-MAIN-2016-18", "CC-MAIN-2016-07", "CC-MAIN-2015-48",
    "CC-MAIN-2015-40", "CC-MAIN-2015-35", "CC-MAIN-2015-32", "CC-MAIN-2015-27",
    "CC-MAIN-2015-22", "CC-MAIN-2015-18", "CC-MAIN-2015-14", "CC-MAIN-2015-11",
    "CC-MAIN-2015-06", "CC-MAIN-2014-52", "CC-MAIN-2014-49", "CC-MAIN-2014-42",
    "CC-MAIN-2014-41", "CC-MAIN-2014-35", "CC-MAIN-2014-23", "CC-MAIN-2014-15",
    "CC-MAIN-2014-10", "CC-MAIN-2013-48", "CC-MAIN-2013-20", "CC-MAIN-2012",
    "CC-MAIN-2009-2010", "CC-MAIN-2008-2009",
]


def request_with_retry(method: str, url: str, **kwargs) -> requests.Response | None:
    """Make HTTP request with exponential backoff retry on 504 errors."""
    backoff = INITIAL_BACKOFF
    for attempt in range(MAX_RETRIES + 1):
        try:
            resp = requests.request(method, url, **kwargs)
            if resp.status_code == 504 and attempt < MAX_RETRIES:
                print(f"  504 Gateway Timeout, retrying in {backoff}s...", file=sys.stderr)
                time.sleep(backoff)
                backoff *= 2
                continue
            return resp
        except requests.RequestException as e:
            if attempt < MAX_RETRIES:
                print(f"  Request failed: {e}, retrying in {backoff}s...", file=sys.stderr)
                time.sleep(backoff)
                backoff *= 2
                continue
            raise
    return None


def search_index(url_pattern: str, crawl_id: str) -> list[dict]:
    """Search a single Common Crawl index for URLs matching pattern."""
    index_url = f"https://index.commoncrawl.org/{crawl_id}-index"
    params = {"url": url_pattern, "output": "json"}

    resp = request_with_retry(
        "GET", index_url,
        params=params,
        headers={"User-Agent": USER_AGENT},
        timeout=30,
    )
    if not resp or resp.status_code != 200:
        status = resp.status_code if resp else "no response"
        print(f"  Error querying {crawl_id}: HTTP {status}", file=sys.stderr)
        return []

    results = []
    for line in resp.text.strip().split("\n"):
        if line:
            try:
                results.append(json.loads(line))
            except json.JSONDecodeError:
                continue

    return results


def fetch_page_content(record: dict) -> bytes | None:
    """Fetch page content from Common Crawl using warcio for proper WARC parsing."""
    offset = int(record["offset"])
    length = int(record["length"])
    s3_url = CC_S3_BASE + record["filename"]
    byte_range = f"bytes={offset}-{offset + length - 1}"

    resp = request_with_retry(
        "GET", s3_url,
        headers={"User-Agent": USER_AGENT, "Range": byte_range},
        stream=True,
        timeout=60,
    )
    if not resp or resp.status_code != 206:
        status = resp.status_code if resp else "no response"
        print(f"  Failed to fetch: HTTP {status}", file=sys.stderr)
        return None

    try:
        for warc_record in ArchiveIterator(resp.raw):
            if warc_record.rec_type == "response":
                return warc_record.content_stream().read()
    except Exception as e:
        print(f"  Error parsing WARC: {e}", file=sys.stderr)
        return None

    return None


def sanitize_filename(url: str, timestamp: str) -> str:
    """Convert URL to a safe filename."""
    parsed = urlparse(url)
    path = parsed.path.strip("/") or "index"
    safe_path = re.sub(r'[<>:"/\\|?*]', "_", path)
    if len(safe_path) > 100:
        safe_path = safe_path[:100]
    return f"{timestamp}_{safe_path}.html"


def download_pages(
    records: list[dict],
    output_dir: str,
    crawl_id: str | None = None,
    limit: int | None = None,
) -> list[dict]:
    """Download pages and save to output directory. Returns list of downloaded files."""
    os.makedirs(output_dir, exist_ok=True)

    download_count = limit if limit else len(records)
    downloaded = []

    for i, record in enumerate(records[:download_count]):
        url = record["url"]
        timestamp = record["timestamp"]
        record_crawl = crawl_id or record.get("crawl_id", "unknown")
        print(f"\n[{i+1}/{download_count}] {url}", file=sys.stderr)

        content = fetch_page_content(record)
        if not content:
            continue

        # Create subdirectory: crawl_id/domain/
        parsed = urlparse(url)
        domain_dir = os.path.join(output_dir, record_crawl, parsed.netloc.replace(":", "_"))
        os.makedirs(domain_dir, exist_ok=True)

        filename = sanitize_filename(url, timestamp)
        filepath = os.path.join(domain_dir, filename)

        with open(filepath, "wb") as f:
            f.write(content)

        print(f"  Saved {len(content):,} bytes -> {filepath}", file=sys.stderr)

        downloaded.append({
            "url": url,
            "timestamp": timestamp,
            "crawl_id": record_crawl,
            "filepath": filepath,
            "size": len(content),
        })

    return downloaded


def process_single_crawl(
    url_pattern: str,
    crawl_id: str,
    output_dir: str,
    download: bool,
    limit: int | None,
) -> tuple[list[dict], list[dict]]:
    """Process a single crawl index. Returns (results, downloaded)."""
    print(f"\n{'='*60}", file=sys.stderr)
    print(f"Searching {crawl_id}...", file=sys.stderr)
    print(f"{'='*60}", file=sys.stderr)

    results = search_index(url_pattern, crawl_id)
    if not results:
        print(f"  No results found in {crawl_id}", file=sys.stderr)
        return [], []

    print(f"  Found {len(results)} results", file=sys.stderr)
    for r in results:
        r["crawl_id"] = crawl_id

    downloaded = []
    if download:
        downloaded = download_pages(results, output_dir, crawl_id, limit)

    return results, downloaded


def main():
    parser = argparse.ArgumentParser(
        description="Search Common Crawl for URLs and download content",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Search and download from a specific crawl
  python commoncrawl_search.py "https://li.st/Bourdain*" -c CC-MAIN-2018-09 --download

  # Search ALL indices, download results organized by crawl ID
  python commoncrawl_search.py "https://li.st/Bourdain*" --all --download

  # Search all indices, limit 10 downloads per crawl
  python commoncrawl_search.py "https://example.com/*" --all --download -l 10

  # Search only (no download), save results to JSON
  python commoncrawl_search.py "https://example.com/*" -c CC-MAIN-2024-51 -o results.json

  # List all available indices
  python commoncrawl_search.py --list-crawls "dummy"
        """,
    )

    parser.add_argument("url_pattern", help="URL pattern to search (supports * wildcard)")
    parser.add_argument(
        "--crawl", "-c", action="append", dest="crawls",
        help="Specific crawl ID(s) to search (can be repeated)",
    )
    parser.add_argument(
        "--all", "-a", action="store_true",
        help="Search ALL crawl indices (2008-2025)",
    )
    parser.add_argument("--output", "-o", help="Output file for search results (JSON)")
    parser.add_argument("--download", action="store_true", help="Download page content")
    parser.add_argument(
        "--dir", "-d", default="./commoncrawl_downloads",
        help="Output directory for downloads (default: ./commoncrawl_downloads)",
    )
    parser.add_argument("--limit", "-l", type=int, help="Limit number of pages to download per crawl")
    parser.add_argument("--list-crawls", action="store_true", help="List available crawl indices")

    args = parser.parse_args()

    if args.list_crawls:
        print("Available crawl indices:")
        for c in CRAWL_INDICES:
            print(f"  {c}")
        return

    # Determine which crawls to search
    if args.all:
        crawl_ids = CRAWL_INDICES
    elif args.crawls:
        crawl_ids = args.crawls
    else:
        parser.error("Specify --crawl/-c or --all/-a to select crawl indices")

    all_results = []
    all_downloaded = []

    for crawl_id in crawl_ids:
        results, downloaded = process_single_crawl(
            args.url_pattern,
            crawl_id,
            args.dir,
            args.download,
            args.limit,
        )
        all_results.extend(results)
        all_downloaded.extend(downloaded)

    print(f"\n{'='*60}", file=sys.stderr)
    print(f"TOTAL: {len(all_results)} results found across {len(crawl_ids)} indices", file=sys.stderr)

    if args.download:
        # Save combined manifest
        os.makedirs(args.dir, exist_ok=True)
        manifest_path = os.path.join(args.dir, "manifest.json")
        with open(manifest_path, "w") as f:
            json.dump(all_downloaded, f, indent=2)
        print(f"Downloaded {len(all_downloaded)} files. Manifest: {manifest_path}", file=sys.stderr)

    if args.output:
        with open(args.output, "w") as f:
            json.dump(all_results, f, indent=2)
        print(f"Results saved to {args.output}", file=sys.stderr)
    elif not args.download:
        for r in all_results:
            print(json.dumps(r))


if __name__ == "__main__":
    main()
