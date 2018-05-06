import logging

SP_BACKGROUND = "sprite/sprite_background.jpg"
SP_END = "sprite/sprite_banana.png"
SP_BEGING = "sprite/sprite_starting.png"
SP_WALL = "sprite/sprite_wall.png"
SP_DKD = "sprite/sprite_dk_bas.png"
SP_DKU = "sprite/sprite_dk_haut.png"
SP_DKR = "sprite/sprite_dk_droite.png"
SP_DKL = "sprite/sprite_dk_gauche.png"

TITLE = "DK Lab"

DIR_TO_MAP = "map"

SPRITE_SIZE = 30

HEIGHT = SPRITE_SIZE * 15
WIDTH = SPRITE_SIZE * 15

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

LOG_LEVEL = [
	logging.CRITICAL,
	logging.ERROR,
	logging.WARNING,
	logging.INFO,
	logging.DEBUG
]
