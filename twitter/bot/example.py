# coding:utf-8

from bot_function import *

def example1():
	bad_words = [' -RT', 'Boston', 'football', 'charlotte', 'amos']
	good_words = ['southend', 'southendonsea', 'southend on sea']
	filter = " OR ".join(good_words)
	blacklist = " -".join(bad_words)
	keywords = filter + blacklist
	ft_show_tweet(ft_search_tweet(keywords, 50))

def main():
	list_fc = ["search tweet"]
	dic_fc = {1:example1}
	while True:
		print("======== Menu =======")
		# print list_fc
		for i, fc in enumerate(list_fc):
			print("{}. {}".format(i + 1, fc))
		er = 1
		# ask user for what the function he want to call
		while er == 1:
			r = input("saisissez l'index de la fonction a exe (-1 pour quitter)\n>>>")
			try:
				res = int(r)
				if res != -1 and (res < 1 or res > len(list_fc)):
					raise ValueError("Error: the index {0} is too {1} the value must be beetween 1 and {2}"\
				.format(res, "small" if res < 1 else "big", len(list_fc)))
			except Exception as e:
				print(e)
			else:
				er = 0
		# quit or lauch the choosen function
		if res == -1:
			break
		else:
			dic_fc[res]()

if __name__ == '__main__':
	main()
