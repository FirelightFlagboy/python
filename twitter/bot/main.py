#coding:utf-8
# Importing the module
from twython import Twython
from time import sleep
from twitter_info import *

#Prepare your twitter, you will need it for everything
twitter = Twython(ft_get_appkey(), ft_get_appsecret(),\
		ft_get_oauthtoken(), ft_get_oauthsecret())
#The above should just be a single line, without the break

#The obligatory first status update to test
def ft_post_twt(status):
	try:
		twitter.update_status(status=status)
		sleep(1)
		print("published :{}".format(status))
	except Exception as e:
		print(e)

def ft_retweet(url):
	try:
		ids = url.split("/")
		twitter.retweet(id=ids[-1])
		sleep(1)
	except Exception as e:
		print(e)

def main():

if __name__ == '__main__':
	main()
