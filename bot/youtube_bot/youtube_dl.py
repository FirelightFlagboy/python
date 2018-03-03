# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import youtube_dl

class MyLogger(object):
	def debug(self, msg):
		# print "debug: "+msg
		pass

	def warning(self, msg):
		print "warning: "+msg

	def error(self, msg):
		print "error: "+msg

def my_hook(d):
	if d['status'] == 'finished':
		print 'Done downloading, now converting ...'

ydl_opts = {
	'format': 'bestaudio/best',
	'outtmpl': '%(title)s.%(ext)s',
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'm4a',
		'preferredquality': '192',
	}],
	'logger': MyLogger(),
	'progress_hooks': [my_hook],
}

def main():
	url_video = 'https://www.youtube.com/watch?v=6_YG9XBX04Y'
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([url_video])

if __name__ == '__main__':
	main()
