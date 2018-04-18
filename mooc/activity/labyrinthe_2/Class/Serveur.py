import select
import socket

class Serveur():
	"""
	La classe du Serveur
	"""
	def __init__(self, strMap, hote="", port=12800):

		# initialise le serveur
		self.main_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.main_connexion.bind((hote, port))
		self.main_connexion.listen(5)

