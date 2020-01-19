from retrivers import retriever
from filters import textfilter
from retrivers import feed_from_chrom_status as getpostfromchrome
from filters import check7days as week_retriever
from htmlcreator import create_html_page as create_html_page
from emailsender import emailgmail
from retrivers import twitter_scra as twitter_tweets
from retrivers import blog as blog

days = twitter_tweets.retrieve_google_sheet_twitter_sites("Days")


# receive each source site array
def send_source_to_check_7days(source):
    tmp_resource = []
    for item in source:
        if isinstance(item, dict):
           if week_retriever.retrieve_post_from_last_week(item['date'], days,source[0]):
               tmp_resource.append(item)
        else:
            tmp_resource.append(item)
    return tmp_resource


def text_filter(url, source):
    if source == "Chromestatus":
        return textfilter.filterposts(send_source_to_check_7days(getpostfromchrome.getposts(url))) # chromestatus
    elif "twitter" in str(source):
        return send_source_to_check_7days(source) #twitter
    elif "web.dev/blog" in(source):
        return send_source_to_check_7days(blog.get_post_from_blog(source)) #web.dev/blog
    else:
        return textfilter.filterposts(send_source_to_check_7days(retriever.getparserposts(url, source))) # other sites

def main():
    sites = []
    resources = []

    my_dict = {
        "Chromeblog": "http://blog.chromium.org/atom.xml",
        "Chromestatus": "https://www.chromestatus.com/features_v2.json",
        "Opera Mobile": "https://blogs.opera.com/mobile/feed",
        "Opera": "https://blogs.opera.com/news/feed",
        "Webkit": "https://webkit.org/blog/feed/atom",
        "Developers Google": "https://developers.google.com/web/updates/rss.xml",
        "Google Webmaster": "http://googlewebmastercentral.blogspot.com/atom.xml",
        "web.dev/blog": "https://web.dev/blog"
    }

    for key in my_dict:
        site_name = my_dict[key]
        if not site_name =="https://web.dev/blog":
            sites.append(site_name[:site_name.rfind("/")])
        else:
            sites.append(site_name)
        source = text_filter(site_name, key)
        resources.append(source)

    for x in twitter_tweets.retrieve():
          # go over twitter accounts
        resources.append(text_filter(None,x))

    create_html_page(resources, days, sites)
    emailgmail.send_mail(days)

if __name__ == "__main__":
    main()
