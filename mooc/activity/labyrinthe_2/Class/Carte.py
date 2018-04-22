import random
from RobotAction import RobotAction

class Carte(RobotAction):

	"""Objet de transition entre un fichier et un labyrinthe."""


	def __init__(self, nom, chaine):
		self.nom = nom
		self.map = chaine
		self.nb_line, self.labyrinthe = self.convStrToLabyrinthe(chaine)

	def convStrToLabyrinthe(chaine):
			"""fonction qui creer un dictionnaire avec les
			coordonnée de chaque 'case' et de son 'type'"""
			dic = {}
			lig = 1
			col = 1
			for char in chaine:	#on lit la chaine char par char
				#on test chaque characteres pour affecter le bon type au dictionnaire
				if char in '\n': #quand on atteind la fin de la ligne, on change de ligne
					lig += 1
					col = 0
				else:
					dic[lig, col] = char

				col += 1

			return (lig, dic)

	def pickRandomLocation(self):
		""" methode qui choisi une zone vide (pas un mur/sortie)
		de maniere aleatoire """
		lab = self.labyrinthe
		# variable qui va contenie toute les coor possible
		coor = []
		for key, val in lab.items():
			if val is " ":
				coor.append(key)
		# si aucun emplacement est vide alors on renvoie null
		if len(coor) is 0:
			return None
		# sinon on choisi une valeur aleatoire parmi toute les coordonnées possible
		return random.choice(coor)

	def robotCanMove(self, coord, count, vector):
		"""
		Test si le robot peut ce deplacer dans une certaine direction
		"""
		xr, yr = coord
		xv, yv = vector
		for i in range(count + 1):
			lt = self.labyrinthe[xr, yr]
			if lt not in " " and lt not in "U":
				return False
			xr += xv
			yr += yv
		return True

	def robotCanWork(self, coord, count, vector, fill):
		"""
		Test si dans la direction choisi le robot
		peut creuser/murer
		"""
		xr, yr = coord
		xv, yv = vector
		xr += xv
		yr += yv
		lt = self.labyrinthe[xr, yr]
		if fill is True and lt in ".":
			return True
		if fill is False and lt in "O":
			return True
		return False

	def actionOk(self, coord, action, direction, count=1):
		"""
		methode qui renvoie vraie si une action commit par un robot
		est possible
		"""
		dd = {
			"n":(-1, 0),
			"s":( 1, 0),
			"e":( 0, 1),
			"o":( 0, -1)
		}
		if action in "nseo":
			return self.robotCanMove(coord, count, dd[direction])
		elif action in "mp":
			return self.robotCanWork(coord, count, dd[direction], action in "m")

	def __repr__(self):
		return "<Carte {}>".format(self.nom)

	def __str__(self):
		return self.map

	convStrToLabyrinthe = staticmethod(convStrToLabyrinthe)
