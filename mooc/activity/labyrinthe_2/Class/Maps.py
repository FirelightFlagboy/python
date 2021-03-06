import os
import sys
import re
from Class.Carte import Carte


class Maps():
	"""
	classe qui permet de recurpere les maps d'un dossier choisi
	"""

	def __init__(self, *args):
		# regex pour verifier le contenue
		self.ex_content = r"^[O.\nU ]+$"
		self.ex_choice = r"^[1-9][0-9]+$"
		# on peut preciser plusieur repertoire ou cherche les fichiers maps
		self.dirToSearch = args
		# variable qui seront initialiser plus tard
		self.maps = []
		self.index = -1
		self.nb_carte = -1

	def displayMenu(self):
		"""
		affiche toute les maps trouver raise une erreur si aucun map
		n'a etait trouver
		"""
		# si il n'y a aucune maps alors on quite
		if self.nb_carte <= 0:
			print("no map found", file=sys.stderr)
			sys.exit(1)
		print("Labytinthes existant :")
		for i, carte in enumerate(self.maps):
			print("  {} - {}".format(i + 1, carte.nom))

	def getMapFromChoice(self):
		"""
		demande a l'utilisateur de choisir une map parmi celle qui existe
		"""
		self.nb_carte = len(self.maps)
		self.displayMenu()
		choice = ""
		while 1:
			while re.search(self.ex_choice, choice) is None:
				choice = input("saisissez un chiffre entre 1 et {}\n>> ".format(self.nb_carte))
			try:
				index = int(choice)
				if index >= 1 and index <= self.nb_carte:
					break
				raise ValueError(
					"Erreur le choix doit etre compris entre 1 et {}".format(self.nb_carte), file=sys.stderr)
			except Exception as e:
				print(e)
			choice = ""
		index += -1
		self.index = index
		return self.maps[index]

	def readFromAgr(self):
		for rep in self.dirToSearch:
			self.maps.extend(self.searchFormDir(rep))
		self.nb_carte = len(self.maps)

	def isMapContentOk(self, map):
		if re.search(self.ex_content, map) is None:
			return False
		if "U" not in map:
			return False
		if " " not in map:
			return False
		return True

	def searchFormDir(self, repertoire):
		"""
		fonction qui lit un repertoire et recuper tout les maps compatible
		"""
		# check if the current working dir exist and is a directory
		if os.path.exists(repertoire) is False:
			print("{} doesn't exist".format(repertoire), file=sys.stderr)
			return []
		if os.path.isdir(repertoire) is False:
			print("{} not a directory".format(repertoire), file=sys.stderr)
			return []
		# if all test pass then work on this repertoire and add the map found to the list map
		maps = []

		for nameFile in os.listdir(repertoire):
			if nameFile.endswith(".txt"):
				path = os.path.join(repertoire, nameFile)
				nameMap = nameFile[:-4].lower()
				with open(path, "r") as mapFile:
					content = mapFile.read()
					if self.isMapContentOk(content):
						maps.append(Carte(nameMap, content))
		return maps
