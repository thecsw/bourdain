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

> Images **have been lost**. Other avenus had struck no luck. I'll try again later.

## Recovering what was lost

From Greg's page, let's go and try each entry one by one, I'll put the table of what I wasn't
able to find in *Common Crawl*, but I would assume exists elsewhere---I'd be happy to take another
look. And no, none of this above has been written by AI, only the code since I don't really care
about `warcio` encoding or writing the same python requests method for the Nth time. Enjoy!

### Things I No Longer Have Time or Patience For

> Recovered HTML in [things-i-no-longer-have-time-or-patience-for](commoncrawl_downloads/CC-MAIN-2018-09/li.st/20180223192051_Bourdain_things-i-no-longer-have-time-or-patience-for-1UsJAtbmYp0qxlBQSLbl2W.html).

1. Cocaine
2. True Detective
3. Scripps Howard
4. Dinners where it takes the waiter longer to describe my food than it takes me to eat it.
5. Beer nerds

### Nice Views

> Recovered HTML in [nice-views](commoncrawl_downloads/CC-MAIN-2017-34/li.st/20170819133925_Bourdain_nice-views-1KMXqnoUWrWiDzcDN7MYZV.html).

I admit it: my life doesn't suck. Some recent views I've enjoyed

1. Montana at sunset : There's pheasant cooking behind the camera somewhere. To the best of my recollection some very nice bourbon. And it IS a big sky .
2. Puerto Rico: Thank you Jose Andres for inviting me to this beautiful beach!
3. Naxos: drinking ouzo and looking at this. Not a bad day at the office .
4. LA: My chosen final resting place . Exact coordinates .
5. Istanbul: raki and grilled lamb and this ..
6. Borneo: The air is thick with hints of durian, sambal, coconut..
7. Chicago: up early to go train #Redzovic

### If I Were Trapped on a Desert Island With Only Three Tv Series

> Recovered HTML in [if-i-were-trapped-on-a-desert-island-with-only-three-tv-series](commoncrawl_downloads/CC-MAIN-2018-09/li.st/20180221100224_Bourdain_if-i-were-trapped-on-a-desert-island-with-only-three-tv-series-6BnoIWYoh1HicApAsKdzVV.html).

1. The Wire
2. Tinker, Tailor, Soldier, Spy (and its sequel : Smiley's People)
3. Edge of Darkness (with Bob Peck and Joe Don Baker )

### The Film Nobody Ever Made

> Recovered HTML in [the-film-nobody-ever-made](commoncrawl_downloads/CC-MAIN-2017-39/li.st/20170925043720_Bourdain_the-film-nobody-ever-made-3mgfdMsKHaJ00f0sYGYlfs.html).

Dreamcasting across time with the living and the dead, this untitled, yet to be written masterwork of cinema, shot, no doubt, by Christopher Doyle, lives only in my imagination.

1. This guy
2. And this guy
3. All great films need:
4. The Oscar goes to..
5. And

> Sorry, each item had a picture attached, they're gone.

### I Want Them Back

> Recovered HTML in [i-want-them-back](commoncrawl_downloads/CC-MAIN-2017-34/li.st/20170817080202_Bourdain_i-want-them-back-5EAiX66WSzxuFJlbJ7cssl.html).

If you bought these vinyls from an emaciated looking dude with an eager, somewhat distracted expression on his face somewhere on upper Broadway sometime in the mid 80's, that was me . I'd like them back. In a sentimental mood.

> There were 11 images here.

### Objects of Desire

> Recovered HTML in [objects-of-desire](commoncrawl_downloads/CC-MAIN-2017-34/li.st/20170820120924_Bourdain_objects-of-desire-205C8woLZ8qID1mskkDn4z.html).

material things I feel a strange, possibly unnatural attraction to and will buy (if I can) if I stumble across them in my travels. I am not a paid spokesperson for any of this stuff .

1. Vintage Persol sunglasses : This is pretty obvious. I wear them a lot. I collect them when I can. Even my production team have taken to wearing them.
2. 19th century trepanning instruments: I don't know what explains my fascination with these devices, designed to drill drain-sized holes into the skull often for purposes of relieving "pressure" or "bad humours". But I can't get enough of them. Tip: don't get a prolonged headache around me and ask if I have anything for it. I do.
3. Montagnard bracelets: I only have one of these but the few that find their way onto the market have so much history. Often given to the indigenous mountain people 's Special Forces advisors during the very early days of America's involvement in Vietnam .
4. Jiu Jitsi Gi's: Yeah. When it comes to high end BJJ wear, I am a total whore. You know those people who collect limited edition Nikes ? I'm like that but with Shoyoroll . In my defense, I don't keep them in plastic bags in a display case. I wear that shit.
5. Voiture: You know those old school, silver plated (or solid silver) blimp like carts they roll out into the dining room to carve and serve your roast? No. Probably not. So few places do that anymore. House of Prime Rib does it. Danny Bowein does it at Mission Chinese. I don't have one of these. And I likely never will. But I can dream.
6. Kramer knives: I don't own one. I can't afford one . And I'd likely have to wait for years even if I could afford one. There's a long waiting list for these individually hand crafted beauties. But I want one. Badly. http://www.kramerknives.com/gallery/
7. R. CRUMB : All of it. The collected works. These Taschen volumes to start. I wanted to draw brilliant, beautiful, filthy comix like Crumb until I was 13 or 14 and it became clear that I just didn't have that kind of talent. As a responsible father of an 8 year old girl, I just can't have this stuff in the house. Too dark, hateful, twisted. Sigh...
8. THE MAGNIFICENT AMBERSONS : THE UNCUT, ORIGINAL ORSON WELLES VERSION: It doesn't exist. Which is why I want it. The Holy Grail for film nerds, Welles' follow up to CITIZEN KANE shoulda, coulda been an even greater masterpiece . But the studio butchered it and re-shot a bullshit ending. I want the original. I also want a magical pony.

> Each bulleted point had an image too.

### Four Spy Novels by Real Spies and One Not by a Spy

> Recovered HTML in [four-spy-novels-by-real-spies-and-one-not-by-a-spy](commoncrawl_downloads/CC-MAIN-2018-09/li.st/20180219155116_Bourdain_four-spy-novels-by-real-spies-and-one-not-by-a-spy-1UsIx7MDcvv7HuPrd2YjM8.html).

I like good spy novels. I prefer them to be realistic . I prefer them to be written by real spies. If the main character carries a gun, I'm already losing interest. Spy novels should be about betrayal.

1. Ashenden--Somerset Maugham
   Somerset wrote this bleak, darkly funny, deeply cynical novel in the early part of the 20th century. It was apparently close enough to the reality of his espionage career that MI6 insisted on major excisions. Remarkably ahead of its time in its atmosphere of futility and betrayal.

2. The Man Who Lost the War--WT Tyler
   WT Tyler is a pseudonym for a former "foreign service" officer who could really really write. This one takes place in post-war Berlin and elsewhere and was, in my opinion, wildly under appreciated. See also his Ants of God.

3. The Human Factor--Graham Greene
   Was Greene thinking of his old colleague Kim Philby when he wrote this? Maybe. Probably. See also Our Man In Havana.

4. The Tears of Autumn -Charles McCarry
   A clever take on the JFK assassination with a Vietnamese angle. See also The Miernik Dossier and The Last Supper

5. Agents of Innocence--David Ignatius
   Ignatius is a journalist not a spook, but this one, set in Beirut, hewed all too closely to still not officially acknowledged events. Great stuff.

## Lost pages

| Title | Date |
|-|-|
| David Bowie Related | 1/14/2016| 
