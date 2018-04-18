# -*-coding:utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os
import re

from carte import Carte
from labyrinthe import Labyrinthe
#si le joueur souhaite faire plusieur partie à la fois
while 1:
	partieEnCours = False
	nbCarte = 0
	choix =" "
	aGagner = False
	# On charge les cartes existantes
	cartes = []
	for nom_fichier in os.listdir("cartes"):
		if nom_fichier.endswith(".txt"):
			chemin = os.path.join("cartes", nom_fichier)
			nom_carte = nom_fichier[:-3].lower()
			with open(chemin, "r") as fichier:
				contenu = fichier.read()
				cartes.append(Carte(nom_carte,contenu))

	# On affiche les cartes existantes
	print("Labyrinthes existants :")
	for i, carte in enumerate(cartes):
		print("  {} - {}".format(i + 1, carte.nom))
		if carte.nom in "last_save.":
			partieEnCours = True
			index_last_save = i+1
		nbCarte += 1
	# Si il y a une partie sauvegardée, on l'affiche
	if partieEnCours:
		print("voulez-vous terminer votre derniere partie ?")
		while choix not in "oui" and choix not in "non":
			choix = input("oui/non\n>")
			choix = choix.lower()

	#si le joueur ne veut pas jouer a son ancienne partie ou qu'on en a pas trouver
	if choix not in "oui" :
		ex = r"^[0-9]+$"
		#on tourne tant que le jouer n'a pas saisi une bonne valeur
		while 1:
			print("pour choisir une carte:")
			while re.search(ex,choix) is None:
					choix = input("saisissez un chiffre compris entre 1 et {}\n>".format(nbCarte))
			try:
				choix = int(choix)
				if choix >= 1 and choix <= nbCarte:
					break
			except TypeError as e:
				raise ValueError("Erreur: impossible de convertir la valeur choix >{} en int".format(choix))
			choix = " "


	#si le joueur veut jouer a son ancienne partie
	else:
		choix = index_last_save
		print(choix)

	#une fois que le joueur a choisi une carte
	try:
		choix = int(choix)
	except TypeError as e:
		raise e("Erreur: impossible de convertir la valeur choix >{} en int".format(choix))

	choix -= 1
	lab = Labyrinthe(cartes[choix].labyrinthe)

	#une fois que le joueur a choisi sa carte,
	#on peut commencer a jouer

	ex = r"^[newsQq]([1-9][0-9]*)?$"

	while aGagner == False:
		#on affiche la carte
		print(lab)
		#on demande au joueur les actions a faire
		print("saisissez une direction (n/e/w/s) ou Q pour quitter:")
		choix = ""
		while re.search(ex, choix) is None:
			choix = input(">")
		#si le jouer ne souhaite pas quitter alors on la continue
		if choix[:1].lower() not in "q":
			#si le joueur a entrer un direction + une valeur
			if len(choix) > 1:
				#on separe la direction et le nb de deplacement a faire
				direction = choix[:1]
				nbRep = choix[1:]
				#on convertie le nb de Rep de type 'str' en 'int'
				try:
					nbRep = int(nbRep)
				except TypeError as e:
					raise e("Erreur: impossible de convertir la valeur nbRep>{}".format(nbRep))
				lab.deplacement(direction, nbRep)
			else:
				lab.deplacement(choix)
			#on verifie si le robot se trouve sur la sortie
			aGagner = lab.RobotOnExit()

			#on enregistre le coup
			chemin = os.path.join("cartes","last_save.txt")
			with open(chemin, "w") as fichier:
				fichier.write(str(lab))

		else :
			#on quitte si le joueur appuye sur 'Q'
			choix = "non"
			break

	#si le joueur a gagne ou decide de partir
	if aGagner:
		print(lab)
		print("Bravo,vous avez gagné")
		#on supprime le ficher 'last_save.txt' car on n'en a plus besoin
		os.remove(chemin)
	while len(choix) < 3 and choix not in "oui" and choix not in "non" and len(choix) > 3:
			choix = input("voulez-vous faire une autre partie ?\noui/non\n>")
			choix = choix.lower()

	if choix in "non" :
		break

print("a plus ;)")

os.system("pause")
