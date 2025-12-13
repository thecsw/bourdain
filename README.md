# Recovering Anthony Bourdain's (really) lost Li.st's.

Loved reading through *GReg TeChnoLogY*'s 
[Anthony Bourdain's Lost Li.st's](https://bourdain.greg.technology/) and seeing
the list of lost Anthony Bourdain li.st's made me think on whether at least *some*
of them are indeed recoverable.

Having worked in security and crawling space for majority of my career---I don't have
the access nor permission to use the proprietary storages---I thought we might be able
to find something from publicly available crawl archives.

## Common Crawl

If *Internet Archive* had the partial list that Greg published, what about the *Common Crawl*?
Reading through their [documentation](https://commoncrawl.org/get-started), it seems
straightforward enough to get prefix index for Tony's lists and grep for any sub-paths.

Putting something up with help of Claude to prove my theory, we have `commoncrawl_search.py`
that makes a single index request to a specific dataset and if any hits discovered, retrieve
them from the public s3 bucket--since they are small straight-up HTML documents, seems even
more feasible than I had initially thought.

Simply have a python version around 3.14.2 and install the dependencies from `requirements.txt`.
Run the below and we are in business. Now, below, you'll find the command I ran and then some
manual archeological effort to prettify the findings.

```sh
python commoncrawl_search.py "https://li.st/Bourdain*" --all --download
```

## Recovering what was lost

From Greg's page, let's go and try each entry one by one, I'll put the table of what I wasn't
able to find in *Common Crawl*, but I would assume exists elsewhere---I'd be happy to take another
look. And no, none of this above has been written by AI, only the code since I don't really care
about `warcio` encoding or writing the same python requests method for the Nth time. Enjoy!

### Things I No Longer Have Time or Patience For

> Recovered HTML in [things-i-no-longer-have-time-or-patience-for](commoncrawl_downloads/CC-MAIN-2018-09/li.st/20180223192051_Bourdain_things-i-no-longer-have-time-or-patience-for-1UsJAtbmYp0qxlBQSLbl2W.html)

1. Cocaine
2. True Detective
3. Scripps Howard
4. Dinners where it takes the waiter longer to describe my food than it takes me to eat it.
5. Beer nerds
