# -*- coding: utf-8 -*-

from os import listdir
from os.path import isfile, join

FOLDER_PATH = "D:\Users\Florian Bennetot\Music"

def enum_music(path):
		onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
		lst = []
		for item in onlyfiles:
			name = item.split('.')
			if name[-1] == 'mp3':
				res = ""
				for i, s in enumerate(name):
					res += (str(s) + ("." if name[i + 1] != 'mp3' else "")) if i < len(name) - 1 else ""
				lst.append(res)
		return (lst)

def main():
	lst = enum_music(FOLDER_PATH)
	for i, name in enumerate(lst):
		print ("{}:\t{}".format(i + 1, name))

if __name__ == '__main__':
	main()
