class RobotAction():
	"""
	La classe qui definit toute les action
	et les direction possible du robot
	c'est valeur sont utilisé en tant que define
	"""
	# les action que peut faire le robot:
	# se deplacer, murer, creuser
	MOVE = 1
	FILL = 2
	DIG = 4
	# les direction du robot:
	# est, ouest, nord, sud
	EAST = 8
	WEST = 16
	NORTH = 32
	SOUTH = 64
