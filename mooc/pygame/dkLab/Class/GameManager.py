import pygame as pg
from copy import deepcopy
import constante as const
from pygame.locals import *
from logging import debug, info, warning, error, critical

class GameManager():

	def __init__(self, lstLab, windows):
		self.ctn = True
		self.choice = False
		self.end = False

		self.lstLab = lstLab
		self.lenLstLab = len(self.lstLab)
		self.windows = windows
		self.lab = None

		self.index = 0

		self.dk = {}
		self.font = {}

		self.fontTitle = pg.font.SysFont("comicsansms", 40)
		self.fontMap = pg.font.SysFont("comicsansms", 40)
		self.fontMapC = pg.font.SysFont("comicsansms", 40)
		self.fontMapC.set_underline(True)

		self.arrowEvent = {
			K_UP:('n', "UP"),
			K_DOWN:('s', "DOWN"),
			K_LEFT:('o', "LEFT"),
			K_RIGHT:('e', "RIGHT")
		}

	def loadSprite(self):
		debug("load sprite image")
		debug("\tlaod dk")

		self.dk = {
			"LEFT":pg.image.load(const.SP_DKL).convert_alpha(),
			"RIGHT":pg.image.load(const.SP_DKR).convert_alpha(),
			"UP":pg.image.load(const.SP_DKU).convert_alpha(),
			"DOWN":pg.image.load(const.SP_DKD).convert_alpha()
		}

		debug("\tdone")
		debug("\tload sprite")

		self.font = {
			"BACK":pg.image.load(const.SP_BACKGROUND).convert(),
			"WALL":pg.image.load(const.SP_WALL).convert(),
			"BEGIN":pg.image.load(const.SP_BEGING).convert(),
			"END":pg.image.load(const.SP_END).convert_alpha(),
			"ICONE":pg.image.load(const.SP_END).convert()
		}

		debug("\tdone")
		debug("done")

		debug("set title and icone")
		pg.display.set_icon(self.font["ICONE"])
		pg.display.set_caption(const.TITLE)

	def renderMap(self, move):

		lmap = self.lab.carte.labyrinthe

		posBegin = self.lab.begin
		posDk = self.lab.robot
		posEx = self.lab.exit

		self.windows.blit(self.font["BACK"], (0, 0))
		for pos, val in lmap.items():
			if val is not "O":
				continue
			x, y = pos
			x *= const.SPRITE_SIZE
			y *= const.SPRITE_SIZE
			self.windows.blit(self.font["WALL"], (y, x))
			x, y = posBegin
		x *= const.SPRITE_SIZE
		y *= const.SPRITE_SIZE
		self.windows.blit(self.font["BEGIN"], (y, x))

		x, y = posEx
		x *= const.SPRITE_SIZE
		y *= const.SPRITE_SIZE
		self.windows.blit(self.font["END"], (y, x))

		x, y = posDk
		x *= const.SPRITE_SIZE
		y *= const.SPRITE_SIZE
		self.windows.blit(self.dk[move], (y, x))

	def addTextChoice(self):
		title = self.fontTitle.render("Dk Lab", True, const.WHITE)
		self.windows.blit(title, title.get_rect(center=(const.WIDTH / 2, 20)))

		for i, lab in enumerate(self.lstLab):
			name = lab.carte.nom
			if i is self.index:
				text = self.fontMapC.render(name, True, const.WHITE)
			else:
				text = self.fontMap.render(name, True, const.WHITE)
			self.windows.blit(text, text.get_rect(center=(const.WIDTH / 2, i * 40 + 60)))

	def updateImageChoice(self):
		self.lab = self.lstLab[self.index]
		self.renderMap("DOWN")

		s = pg.Surface((const.WIDTH, const.HEIGHT))
		s.set_alpha(172)
		s.fill(const.BLACK)
		self.windows.blit(s, (0, 0))
		self.addTextChoice()
		pg.display.flip()

	def workEventChoice(self, lstEvent):
		for event in lstEvent:
			if event.type == QUIT:
				self.ctn = False
			elif event.type == KEYDOWN:
				key = event.key
				if key == K_DOWN:
					self.index += 1
					if self.index >= self.lenLstLab:
						self.index = 0
					debug("index increase to {}".format(self.index))
				elif key == K_UP:
					self.index -= 1
					if self.index < 0:
						self.index = self.lenLstLab - 1
					debug("index decrease to {}".format(self.index))
				elif key == K_RETURN or key == K_KP_ENTER:
					self.choice = True
					debug("user choice map at {}".format(self.index))

	def workEventGame(self, lstEvent, moveW):
		for event in lstEvent:
			if event.type == QUIT:
				self.ctn = False
			elif event.type == KEYDOWN:
				key = event.key
				if key in self.arrowEvent.keys():
					direction, move = self.arrowEvent[key]
					self.lab.canMove(direction)
					moveW[0] = move
				elif key == K_ESCAPE:
					self.end = True

	def getChoiceMap(self):
		self.choice = False
		while self.ctn is True and self.choice is False:
			pg.time.Clock().tick(30)
			self.workEventChoice(pg.event.get())
			self.updateImageChoice()
		self.lab = deepcopy(self.lab)

	def playGame(self):
		self.end = False
		move = ["DOWN"]
		while self.end is False and self.ctn is True:
			pg.time.Clock().tick(30)
			self.workEventGame(pg.event.get(), move)
			self.renderMap(move[0])
			pg.display.flip()
			if self.lab.RobotOnExit() is True:
				self.end = True
