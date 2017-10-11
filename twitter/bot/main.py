#coding:utf-8
# Importing the module twython
from twython import Twython
from time import sleep
from twitter_info import *
import sys

#Prepare your twitter, you will need it for everything
twitter = Twython(ft_get_appkey(), ft_get_appsecret(),\
		ft_get_oauthtoken(), ft_get_oauthsecret())
#The above should just be a single line, without the break

def ft_post_twt(status):
	"""post the str in status to the twitter profile linked"""
	try:
		twitter.update_status(status=status)
		sleep(1)
		print("published :{}".format(status))
	except Exception as e:
		print(e)

def ft_retweet(url):
	"""retweet the post at the url give in params"""
	try:
		ids = url.split("/")
		twitter.retweet(id=ids[-1])
		sleep(1)
	except Exception as e:
		print(e)
	except TwythonError as e:
		print(e)

def ft_search_tweet(ph, count=10):
	"""
	return the result of the search of tweet
	that match ph
	count is the nb max of match to be return
	"""
	return twitter.search(q=ph, count=count)

def ft_show_tweet(result):
	"""
	show all content of tweet contains in result
	"""
	utf8stdout = open(1, 'w', encoding='utf-8', closefd=False) # fd 1 is stdout
	for i, tweet in enumerate(result["statuses"]):
		print("tweet {}:\n{}\n".format(i + 1,tweet["text"]), file=utf8stdout)

def ft_auto_retweet(ph, count=10):
	"""
	auto retweet tweet that match ph
	count is the nb max to be retweet
	"""
	search = ft_search_tweet(ph, count)
	try:
		for tweet in search_result["statuses"]:
			ft_retweet(tweet["id_str"])
	except Exception as e:
		print(e)

def main():
	ft_show_tweet(ft_search_tweet("FireFlagboy", 1000))

if __name__ == '__main__':
	""" call the main() function"""
	main()
