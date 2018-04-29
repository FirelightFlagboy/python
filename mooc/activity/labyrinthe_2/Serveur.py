from Class.Carte import Carte
from Class.Maps import Maps
from Class.Robot import Robot
from Class.Serveur import Serveur
import socket
import select
import os
import sys
import signal

# le repertoire ou se trouve les maps
dirToMap = "map"
# nom de l'hote
hote = ""
# port du serveur
port = 12800
# class serveur
sev = None

def sigint_handler(n, stack):
	global sev
	if sev:
		del sev
	sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

"""
on choisi la map
"""
maps = Maps(dirToMap)
maps.readFromAgr()
carte = maps.getMapFromChoice()
del maps

sev = Serveur(carte, hote, port)
del carte

sev.getClient()
del sev
