#coding:utf-8

from bot_function import *
from data_file import *
from twitter_info import *
from time import sleep
import random

def ft_get_list():
	"""
	get the list of quotes that contains 'quotes.txt'
	"""
	file_n = ft_get_file_name()
	try:
		f = open(file_n, 'r')
	except Exception as e:
		print (e)
	else:
		content = f.read()
		return content.split("\n")
	exit()

def ft_get_rand_quote(ls):
	"""
	return a random quotes
	"""
	return ls[random.randint(0, len(ls) - 1)]

def ft_sleep(hour=0, minu=0, sec=0):
	"""
	simple improved sleep funtion
	"""
	time_to_wait = hour*3600 + minu*60 + sec
	print("wait {} sec".format(time_to_wait))
	sleep(time_to_wait)

def main():
	"""
	main function that send tweet every hour
	"""
	global twitter
	ft_connect_twitter()
	ls = ft_get_list()
	while True:
		src = ft_get_rand_quote(ls)
		ft_auto_retweet("Playwarframe", count=10, result_type="people")
		ft_post_twt(src)
		ft_sleep(hour=1)

if __name__ == '__main__':
	"""
	call the main function
	"""
	main()
