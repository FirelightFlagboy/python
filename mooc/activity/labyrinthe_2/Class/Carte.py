class Carte():

	"""Objet de transition entre un fichier et un labyrinthe."""


	def __init__(self, nom, chaine):
		self.nom = nom
		self.map = chaine
		self.nb_line, self.labyrinthe = self.convStrToLabyrinthe(chaine)

	def __repr__(self):
		return "<Carte {}>".format(self.nom)

	def convStrToLabyrinthe(chaine):
			"""fonction qui creer un dictionnaire avec les
			coordonnée de chaque 'case' et de son 'type'"""
			dic = {}
			lig = 1
			col = 1
			for char in chaine:	#on lit la chaine char par char
				#on test chaque characteres pour affecter le bon type au dictionnaire

				if char in '\n': #quand on attiend la fin de la ligne, on change de colonne
					lig += 1
					col = 0
				else:
					dic[lig,col] = char

				col += 1
			return (lig, dic)

	def __str__(self):
		return self.map

	convStrToLabyrinthe = staticmethod(convStrToLabyrinthe)
