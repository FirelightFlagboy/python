#coding:utf-8
# Importing the module twython
from twython import Twython
from time import sleep, time, strftime
from twitter_info import *
import sys

#Prepare your twitter, you will need it for everything
twitter = 0
#The above should just be a single line, without the break
def ft_connect_twitter():
	"""
	connect the global var 'twitter' to twitter api
	"""
	global twitter
	twitter = Twython(ft_get_appkey(), ft_get_appsecret(),\
			ft_get_oauthtoken(), ft_get_oauthsecret())

def ft_reset_limit_rate():
	"""
	wait the time the reset the rate when to much
	request is done
	"""
	remainder = float(twitter.get_lastfunction_header(header='x-rate-limit-reset')) - time()
	print(remainder)
	sleep(remainder)
	ft_connect_twitter()

def ft_post_twt(status):
	"""post the str in status to the twitter profile linked"""
	try:
		twitter.update_status(status=status)
		sleep(1)
		print("{} publish :\n{}".format(strftime("%d/%m/%y %H:%M:%S"),status))
	except Exception as e:
		print(e)

def ft_retweet(url):
	"""
	retweet the post at the url give in params
	"""
	try:
		ids = url.split("/")
		twitter.retweet(id=ids[-1])
		sleep(1)
	except Exception as e:
		print(e)
	except TwythonError as e:
		print(e)

def ft_favorite(url):
	"""
	fav the post at the url given in params
	"""
	try:
		ids = url.split("/")
		twitter.create_favorite(id=ids[-1])
		sleep(1)
	except Exception as e:
		print(e)
	except TwythonError as e:
		print(e)

def ft_search_tweet(ph, count=10, result_type="recent"):
	"""
	return the result of the search of tweet
	that match ph
	count is the nb max of match to be return
	twitter.search(q="your phrase to be search", count="nb max of match",
	geocode="longitude,etc", lang="language", locale="query's language"
	result_type="recent,etc", until="before date", since_id="more recent than this tweet",
	max_id="older than this tweet", includes_entities="")
	"""
	return twitter.search(q=ph, count=count, result_type=result_type)

def ft_show_tweet(result):
	"""
	show all content of tweet contains in result
	"""
	utf8stdout = open(1, 'w', encoding='utf-8', closefd=False) # fd 1 is stdout
	for i, tweet in enumerate(result["statuses"]):
		print("tweet {}:\n{}\n".format(i + 1,tweet["text"]), file=utf8stdout)

def ft_auto_retweet(ph, count=10, result_type="recent"):
	"""
	auto retweet tweet that match ph
	count is the nb max to be retweet
	"""
	search = ft_search_tweet(ph, count, result_type)
	try:
		for tweet in search["statuses"]:
			ft_retweet(tweet["id_str"])
	except Exception as e:
		print(e)

def ft_auto_fav(ph, count=10):
	"""
	count is the nb max to be fav
	"""
	search = ft_search_tweet(ph, count)
	try:
		for tweet in search["statuses"]:
			ft_favorite(tweet["id_str"])
	except Exception as e:
		print(e)

def main():
	pass

if __name__ == '__main__':
	""" call the main() function"""
	main()
