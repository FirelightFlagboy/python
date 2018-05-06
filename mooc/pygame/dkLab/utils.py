import os
import re
import argparse
import constante as const
from logging import debug, info, warning, error, critical
from Class.Carte import Carte

def parseArg():
	parser = argparse.ArgumentParser()
	parser.add_argument("-v", "--verbosity", default=1,
	type=int, help="increase ouput verbosity", choices=[1, 2, 3, 4, 5])
	return parser.parse_args()

def getMapFromDir(directory):
	"""lit dans le repertoire donnée"""

	debug("read form dir %s", directory)
	lstCarte = []
	# on parcoure le dossier
	for nom_fichier in os.listdir(directory):
		# si le fichier se termine par .txt
		if nom_fichier.endswith(".txt"):
			chemin = os.path.join(directory, nom_fichier)
			nom_carte = nom_fichier[:-3].lower()
			# on ouvre le fichier pour le lire
			with open(chemin, "r") as fichier:
				contenu = fichier.read()
				lstCarte.append(Carte(nom_carte,contenu))
	return lstCarte
