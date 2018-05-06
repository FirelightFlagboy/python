# -*-coding:utf-8 -*

"""Ce module contient la classe Carte."""

class Carte:

	"""Objet de transition entre un fichier et un labyrinthe."""


	def __init__(self, nom, chaine):
		self.nom = nom
		self.chaine = chaine
		self.labyrinthe = self.convStrToLabyrinthe(chaine)

	def __repr__(self):
		return "<Carte {}>".format(self.nom)

	def __str__(self):
		return self.chaine

	def convStrToLabyrinthe(chaine):
			"""fonction qui creer un dictionnaire avec les
			coordonnée de chaque 'case' et de son 'type'"""
			dic = {}
			ligne = 0
			colonne = 0
			for char in chaine:	#on lit la chaine char par char
				#on test chaque characteres pour affecter le bon type au dictionnaire

				if char in '\n': #quand on attiend la fin de la ligne, on change de colonne
					colonne += 1
					ligne = 0
				else:
					dic[colonne,ligne] = char
					ligne += 1

			return dic

	convStrToLabyrinthe = staticmethod(convStrToLabyrinthe)
