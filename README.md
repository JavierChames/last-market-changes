# Market_Changes_NI
 Retrieve changes in several sites and create HTML report

 This project use:Python(3.7) to retrieve post from this sites(rss/atom/xml):
 
       "Chromeblog": "http://blog.chromium.org/atom.xml",
       "Chromestatus": "https://www.chromestatus.com/features_v2.json",
       "Opera Mobile": "https://blogs.opera.com/mobile/feed",
       "Opera": "https://blogs.opera.com/news/feed",
       "Webkit": "https://webkit.org/blog/feed/atom",
       "Developers Google": "https://developers.google.com/web/updates/rss.xml",
       "Google Webmaster": "http://googlewebmastercentral.blogspot.com/atom.xml",
       "web.dev/blog": "https://web.dev/blog"


    in order to install it in a new mahcine please install the required modules in requirements.txt
    pip install -r requirements.txt

    there is also a twitter retriever(accounts configured in google sheet)
    https://docs.google.com/spreadsheets/d/12WmWC2CMwu0wS4Ub8dJwh3dikvfK0SpWYvLyCtRhnr8/edit#gid=1531116104

    the posts(raw data) are filtered according to days & specific words(if enabled)
    the tweets from twitter are also filtered and can be configured the number of tweets to retrieve

    finally all the data passed to module that creates and HTML page,and send it by email to recipients.

