# Recovering Anthony Bourdain's (really) lost Li.st's.

Loved reading through *GReg TeChnoLogY*'s 
[Anthony Bourdain's Lost Li.st's](https://bourdain.greg.technology/) and seeing
the list of lost Anthony Bourdain li.st's made me think on whether at least *some*
of them we can recover.

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

Any and all emphasis, missing punctuation, cool grammar is all by Anthony Bourdain. The only
modifications I have made is to the layout, to represent `li.st` as closely as possible with 
**no changes to the content.**

> If you see these blocks, that's me commenting if pictures have been lost.

## Recovering what we lost

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

1. Ashenden--Somerset Maugham <br/>
   Somerset wrote this bleak, darkly funny, deeply cynical novel in the early part of the 20th century. It was apparently close enough to the reality of his espionage career that MI6 insisted on major excisions. Remarkably ahead of its time in its atmosphere of futility and betrayal.

2. The Man Who Lost the War--WT Tyler <br/>
   WT Tyler is a pseudonym for a former "foreign service" officer who could really really write. This one takes place in post-war Berlin and elsewhere and was, in my opinion, wildly under appreciated. See also his Ants of God.

3. The Human Factor--Graham Greene <br/>
   Was Greene thinking of his old colleague Kim Philby when he wrote this? Maybe. Probably. See also Our Man In Havana.

4. The Tears of Autumn -Charles McCarry <br/>
   A clever take on the JFK assassination with a Vietnamese angle. See also The Miernik Dossier and The Last Supper

5. Agents of Innocence--David Ignatius <br/>
   Ignatius is a journalist not a spook, but this one, set in Beirut, hewed all too closely to still not officially acknowledged events. Great stuff.
   
## Hotel Slut (That's Me)

> Recovered HTML in [hotel-slut-that-s-me](commoncrawl_downloads/CC-MAIN-2020-05/li.st/20200122120527_Bourdain_hotel-slut-that-s-me-6mxRnOOzqQizcDuaTN9mjr.html).

I wake up in a lot of hotels, so I am fiercely loyal to the ones I love. A hotel where I know immediately wher I am when I open my eyes in the morning is a rare joy. Here are some of my favorites

1. CHATEAU MARMONT ( LA) : if I have to die in a hotel room, let it be here. I will work in LA just to stay at the Chateau.
2. CHILTERN FIREHOUSE (London): Same owner as the Chateau. An amazing Victorian firehouse turned hotel. Pretty much perfection
3. THE RALEIGH (Miami): The pool. The pool!
4. LE CONTINENTAL (Saigon): For the history.
5. HOTEL OLOFSSON (Port au Prince): Sagging, creaky and leaky but awesome .
6. PARK HYATT (Tokyo): Because I'm a film geek.
7. EDGEWATER INN (Seattle): kind of a lumber theme going on...ships slide right by your window. And the Led Zep "Mudshark incident".
8. THE METROPOLE (Hanoi): there's a theme developing: if Graham Greene stayed at a hotel, chances are I will too.
9. GRAND HOTEL D'ANGKOR (Siem Reap): I'm a sucker for grand, colonial era hotels in Asia.
10. THE MURRAY (Livingston,Montana): You want the Peckinpah suite

### Steaming Hot Porn

> Recovered HTML in [steaming-hot-porn](commoncrawl_downloads/CC-MAIN-2018-09/li.st/20180225123714_Bourdain_steaming-hot-porn-5hqohJ4af5blrHINxY8OqM.html).

from my phone

1. Bun Bo Hue
2. Kuching Laksa
3. Pot au Feu
4. Jamon
5. Linguine
6. Meat
7. Dessert
8. Light Lunch
9. Meat on a Stick
10. Oily Little Fish
11. Snack
12. Soup
13. Homage
    
> Pictures in each have not been recovered.

### 5 Photos on My Phone, Chosen at Random

> Recovered HTML in [5-photos-on-my-phone-chosen-at-random](commoncrawl_downloads/CC-MAIN-2017-39/li.st/20170923054957_Bourdain_5-photos-on-my-phone-chosen-at-random-0nsXCpUt69UbZvcMsOh4P3.html).

Not TOO random

1. Madeline
2. Beirut
3. Musubi
4. BudaeJiggae
5. Dinner

> Shame, indeed, no pictures, there was one for each.

### People I’d Like to Be for a Day

> Recovered HTML in [people-i-d-like-to-be-for-a-day](commoncrawl_downloads/CC-MAIN-2018-09/li.st/20180223011432_Bourdain_people-i-d-like-to-be-for-a-day-6RzWK74FUhdiWyRc1GTaeM.html).

1. Bootsy Collins
2. Bill Murray

### I'm Hungry and Would Be Very Happy to Eat Any of This Right Now

> Recovered HTML in [i-m-hungry-and-would-be-very-happy-to-eat-any-of-this-right-now](commoncrawl_downloads/CC-MAIN-2018-09/li.st/20180222071826_Bourdain_i-m-hungry-and-would-be-very-happy-to-eat-any-of-this-right-now-1pp6u1q4z0aDg3e4LOVbMn.html).

1. Spaghetti a la bottarga . I would really, really like some of this. Al dente, lots of chili flakes
2. A big, greasy double cheeseburger. No lettuce. No tomato. Potato bun.
3. A street fair sausage and pepper hero would be nice. Though shitting like a mink is an inevitable and near immediate outcome
4. Some uni. Fuck it. I'll smear it on an English muffin at this point.
5. I wonder if that cheese is still good?

### Observations From a Beach

> Recovered HTML in [observations-from-a-beach](commoncrawl_downloads/CC-MAIN-2017-30/li.st/20170722185829_Bourdain_observations-from-a-beach-0X3d0NujKKomnM2HIukguv.html).

In which my Greek idyll is Suddenly invaded by professional nudists

1. Endemic FUPA. Apparently a prerequisite for joining this outfit.
2. Pistachio dick
3. 70's bush
4. T-shirt and no pants. Leading one to the obvious question : why bother?

### Guilty Pleasures

> Recovered HTML in [guilty-pleasures](commoncrawl_downloads/CC-MAIN-2017-34/li.st/20170819134549_Bourdain_guilty-pleasures-1UslAzn8zE50JJvhbBmMmu.html).

1. Popeye's Mac and Cheese
2. The cheesy crust on the side of the bowl of Onion Soup Gratinee
3. Macaroons . Not macarons . Macaroons
4. Captain Crunch
5. Double Double Animal Style
6. Spam Musubi
7. Aerosmith

### Some New York Sandwiches

> Recovered HTML in [some-new-york-sandwiches](commoncrawl_downloads/CC-MAIN-2017-34/li.st/20170823084629_Bourdain_some-new-york-sandwiches-1UsJj9WoWSEIEEAhdMu2EK.html).

Before he died, Warren Zevon dropped this wisdom bomb: "Enjoy every sandwich". These are a few locals I've particularly enjoyed:

1. PASTRAMI QUEEN: (1125 Lexington Ave. ) Pastrami Sandwich. Also the turkey with Russian dressing is not bad. Also the brisket.
2. EISENBERG'S SANDWICH SHOP: ( 174 5th Ave.) Tuna salad on white with lettuce. I'd suggest drinking a lime Rickey or an Arnold Palmer with that.
3. THE JOHN DORY OYSTER BAR: (1196 Broadway) the Carta di Musica with Bottarga and Chili is amazing. Is it a sandwich? Yes. Yes it is.
4. RANDOM STREET FAIRS: (Anywhere tube socks and stale spices are sold. ) New York street fairs suck. The same dreary vendors, same bad food. But those nasty sausage and pepper hero sandwiches are a siren song, luring me, always towards the rocks. Shitting like a mink almost immediately after is guaranteed but who cares?
5. BARNEY GREENGRASS : ( 541 Amsterdam Ave.) Chopped Liver on rye. The best chopped liver in NYC.

### Great Dead Bars of New York

> Recovered HTML in [great-dead-bars-of-new-york](commoncrawl_downloads/CC-MAIN-2017-34/li.st/20170821045245_Bourdain_great-dead-bars-of-new-york-1UsJAwt2gvx85J4MeUca5A.html).

A work in progress

1. SIBERIA in any of its iterations. The one on the subway being the best
2. LADY ANNES FULL MOON SALOON a bar so nasty I'd bring out of town visitors there just to scare them
3. THE LION'S HEAD old school newspaper hang out
4. KELLY'S on 43rd and Lex. Notable for 25 cent drafts and regularly and reliably serving me when I was 15
5. THE TERMINAL BAR legendary dive across from port authority
6. BILLY'S TOPLESS (later, Billy's Stopless) an atmospheric, working class place, perfect for late afternoon drinking where nobody hustled you for money and everybody knew everybody. Great all-hair metal jukebox . Naked breasts were not really the point.
7. THE BAR AT HAWAII KAI. tucked away in a giant tiki themed nightclub in Times Square with a midget doorman and a floor show. Best place to drop acid EVER.
8. THE NURSERY after hours bar decorated like a pediatrician's office. Only the nursery rhyme characters were punk rockers of the day.

## Lost page

It was surprising to see that only one page was not recoverable from the common crawl.

| Title | Date |
|-|-|
| David Bowie Related | 1/14/2016|

# What's next?

I've enjoyed this little project tremendously---a little archeology project. Can we declare victory for at least this 
endeavor? Hopefully, we would be able to find images, but that's a little tougher, since that era's cloudfront is fully
gone.

What else can we work on restoring and setting up some sort of a public archive to store them? I made this a git repository
for the sole purpose so that anyone interested can contribute their interest and passion for these kinds of projects.

Thank you and until next time!
