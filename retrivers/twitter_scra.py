import tweepy 
import dateutil.parser
from datetime import datetime
import json
import os,sys,platform
from  googlesheet  import googlesheet as retrievegs

sys.path.append('../')
if not(platform.system()== "Windows"):
	jsoncredentials=os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'config/twitter/twitter_api_cred.txt'))
else:
	jsoncredentials=os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'config\\twitter\\twitter_api_cred.txt'))


sh=retrievegs.googlesheetconnection()

data=[]


with open(jsoncredentials,'r') as json_file:
	cred = json.load(json_file)
consumer_key=cred['consumer_key']
consumer_secret=cred['consumer_secret']
access_key=cred['access_key']
access_secret=cred['access_secret']

def retrieve_google_sheet_twitter_sites(tab_name): #This function retrieve from google sheets,the twitter accounts we need to search for posts
	if tab_name == "Twitter":
		sheet = sh.worksheet("Twitter")
		values_list = sheet.col_values(1)
		num_tweets=sheet.col_values(2)
		return values_list,num_tweets
	elif tab_name == "Days" :
		sheet = sh.worksheet("Days")
		days = sheet.col_values(1)
		return int(days[0])
sites,num_tweets=retrieve_google_sheet_twitter_sites("Twitter")
# Function to extract tweets 
def get_tweets(tweet_account,x): 
		
		# Authorization to consumer key and consumer secret 
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

		# Access to user's access key and access secret 
		auth.set_access_token(access_key, access_secret) 

		# Calling api 
		api = tweepy.API(auth) 

		# x tweets to be extracted 
		tweetdata=[]
		tweetdata.append("twitter.com/"+tweet_account)
		try:
			tweets = api.user_timeline(screen_name=tweet_account,count=int(num_tweets[x]))
			for tweet in tweets:
				if(len(tweet.entities['user_mentions']) == 0):
					if(len(tweet.entities['urls'])>0):
						tweetdata.append({
							'date':str(tweet.created_at.strftime('%d/%m/%Y')),
							'post':tweet.text.encode("ascii", errors="ignore").decode().split(" https")[0] +"......" ,
							'link':tweet.entities['urls'][0]['url']
							})
			return tweetdata
		except Exception:
				tweetdata.append("Failed retrieving from account:" + tweet_account + " doesnt exists")
				return tweetdata
		

def retrieve():
		x=0
		for tweets_per_account in sites:
			data.append(get_tweets(tweets_per_account,x))
			x+=1
		return data
