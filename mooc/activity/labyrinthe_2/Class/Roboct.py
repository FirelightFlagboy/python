from RobotAction import RobotAction

class Robot(RobotAction):
	"""
	La classe robot:
		- contient les coordonnées du robot
		- sont identifient
		- ses actions en cours
	"""
	def __init__(self, x, y, identifient):
		# la coordonnée x et y du robot sur la map
		self.x = x
		self.y = y
		# l'identifient du robot
		self.identifient = identifient
		# sont action en cours, ainsi que la direction et le nombre de fois
		# qu'elle doit ce repeter
		self.action = None
		self.direction = None
		self.remain = 0

	def needMovement(self):
		"""
		methode qui renvoie vraie si le robot a besoin de commande de la part de
		l'utilisateur
		"""
		if self.action is None or self.direction is None or self.remain is 0:
			return True
		return False

	# a deplacer dans le client
	def checkCommande(self):
		"""
		methode qui check si la commande est bien formater
		"""
		pass

	def checkMovement(self);
		"""
		methode qui check si le movement est possible
		"""
		pass

	def setMovement(self, commande):
		"""
		methode qui set la commande saisi par l'utilisateur
		sur le robot
		"""
		pass


