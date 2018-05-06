
"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

	"""Classe représentant un labyrinthe."""

	def __init__(self, carte):
		"""lab contient toute les coordonne de chaque elment de la map"""
		self.carte = carte

		#on cherche la position du robot dans la map
		for pos, val in self.carte.labyrinthe.items():
			if val in "X":
				self.begin = pos
				self.robot = pos
				self.carte.labyrinthe[pos] = " "
			elif val in "U":
				self.exit = pos

		self.move = {
			'n':(-1, 0),
			's':( 1, 0),
			'e':( 0, 1),
			'o':( 0,-1)
		}

	def __repr__(self):
		"""Quand on entre notre objet dans l'interpreteur"""
		return self.carte.__repr__()

	def __str__(self):
		""" quand on souhaite afficher la map
		grâce à un print, on retourne juste sur
		la fonction __repr__"""
		colonne = 0
		chaine = ""
		for pos, val in self.carte.labyrinthe.items():

			a, b = pos  #on separe les valeur du tuple,
						#'a' simbolise la colonne et 'b' la ligne
			#quand on arrive a une nouvel ligne
			if a != colonne:
				chaine += "\n"
				colonne = a

			#quand on trouve le robot on verifie si il est bien a la bonne position
			if pos == self.begin:
				val = "X"
			if pos == self.robot:
				val = "D"
			# if val in "X" and pos != self.robot:
			# 	val = " "

			chaine += val

		return chaine

	def deplacement(self, direction, nbRep = 1):
		"""permer le deplacement du robot dans une direction donné"""
		for i in range(nbRep):
			#si la voie est libre, on bouge
			self.canMove(direction)


	def canMove(self,direction):
		"""test si le robot peut se deplacer dans la dite direction"""
		x, y = self.robot
		#si on veut aller vers le nord
		if direction not in self.move.keys():
			return False
		xv, yv = self.move[direction]
		x += xv
		y += yv
		if (x, y) in self.carte.labyrinthe.keys() and self.carte.labyrinthe[x, y] is not "O":
			self.robot = (x, y)
			return True
		return False


	def RobotOnExit(self):
		"""verifie si le robot ce trouve sur la porte de sortie"""
		if self.robot == self.exit:
			return True
		else:
			return False
