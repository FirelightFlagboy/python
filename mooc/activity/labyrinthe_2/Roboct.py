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

