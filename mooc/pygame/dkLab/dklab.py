import pygame as pg
import logging as lg
import utils
import constante as const
from Class.GameManager import GameManager
from Class.Labyrinthe import Labyrinthe

args = utils.parseArg()

lg.basicConfig(level=const.LOG_LEVEL[args.verbosity - 1])

lg.debug("search map in folder {}".format(const.DIR_TO_MAP))

lstCarte = utils.getMapFromDir(const.DIR_TO_MAP)
lstLab = []
for ct in lstCarte:
	lstLab.append(Labyrinthe(ct))

lg.debug("lstCarte : {}".format(lstCarte))

pg.init()
fenetre = pg.display.set_mode((const.WIDTH, const.HEIGHT))

msg = "\n"
for lb in lstLab:
	msg += lb.__repr__() + "\n" + lb.__str__() + "\n"
lg.info("tab :\n{}".format(msg))

game = GameManager(lstLab, fenetre)
game.loadSprite()
while game.ctn is True:
	game.getChoiceMap()
	game.playGame()
