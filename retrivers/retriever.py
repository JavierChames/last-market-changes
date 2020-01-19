import feedparser
import dateutil.parser

def getparserposts(site,name): #Parse each site(rss/atom) and retireve array with date,post & link

    NewsFeed = feedparser.parse(site)
    posts= NewsFeed.entries

    data=[]
    data.append(name) 
    if len(posts)==0: # if the site doesnt contain any post(raw data)-we write it in the array and return
        data.append("Failed to retrieve posts")
        return data
    for entry in posts:
        date_post_date_time=dateutil.parser.parse(entry.published).date()
        link=entry['link']
        data.append({
                    'date':date_post_date_time,
                    'post':entry.title,
                    'link':link})
    return data
