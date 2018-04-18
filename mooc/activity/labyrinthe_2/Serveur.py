# from CLass.Serveur import Serveur

import os
import re
from Class.Carte import Carte

dirToMap = "map"
maps = []

for nameFile in os.listdir(dirToMap):
	if nameFile.endswith(".txt"):
		path = os.path.join(dirToMap, nameFile)
		nameMap = nameFile[:-3].lower()
		with open(path, "r") as mapFile:
			content = mapFile.read()
			maps.append(Carte(nameMap, content))

print("Labytinthes existant :")
for i, carte in enumerate(maps):
	print("  {} - {}".format(i + 1, carte.nom))

ex = r"^[0-9]+$"
nb_carte = len(maps)
choice = ""
while 1:
	while re.search(ex, choice) is None:
		choice = input("saisissez un chiffre entre 1 et {}\n>> ".format(nb_carte))
	try:
		index = int(choice)
		if index >= 1 and index <= nb_carte:
			break
		raise ValueError("Erreur le choix doit etre compris entre 1 et {}".format(nb_carte))
	except Exception as e:
		print(e)
	choice = ""
