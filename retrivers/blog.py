import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import parser
import logging


def get_post_from_blog(site):
    posts=[]
    post_dates=[]
    post_names=[]
    post_links=[]
    posts.append("web.dev")
    try:
        page =requests.get("https://"+site)
    except:
        posts.append("Failed to retrieve posts")
        return posts
    soup = BeautifulSoup(page.content, 'html.parser')

    main_div=soup.find('div', class_='w-grid__columns w-grid__columns--three')

    for date in main_div.find_all('div', class_='w-author__published'):
        date=datetime.date(parser.parse(date.text.strip()))
        post_dates.append(date)

    for title in main_div.find_all('h2', class_='w-post-card__headline--with-image'):
        post_names.append(title.text.strip())

    for links in main_div.find_all('a', href=True):
        post_links.append(site.replace('/blog','') + links['href'])

    for i in range(len(post_names)):
            posts.append({
                        'date':post_dates[i],
                        'post':post_names[i],
                        'link':post_links[i]})
    return posts