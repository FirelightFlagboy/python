import pygame as pg
import signal
import os
from pygame.locals import *
from time import sleep
# initialise tous les modules
pg.init()

width = 550
height = 441

fenetre = pg.display.set_mode((width, height))
fond = pg.image.load("doritos.jpg").convert()
fenetre.blit(fond, (0, 0))
ctn = True
pg.display.flip()
def handler(n, stack):
	print("here")
	global ctn
	ctn = False
	os.kill(os.getpid(), signal.SIGTERM)

signal.signal(signal.SIGINT, handler)
while ctn is True:
	sleep(0.05)
	for event in pg.event.get():
		tt = event.type
		if tt == QUIT:
			ctn = False
		elif tt == KEYDOWN:
			print("keydown")
