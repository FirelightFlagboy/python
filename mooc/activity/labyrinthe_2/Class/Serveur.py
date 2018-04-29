import select
import socket
import re
import sys
import os
from Class.Robot import Robot
from Class.Carte import Carte
from Class.Maps import Maps

class Serveur():
	"""
	La classe du Serveur
	"""
	def __init__(self, carte, hote="", port=12800):
		"""
		initialise le serveur
		"""

		self.port = port
		self.hote = hote

		self.lstClient = []
		self.lstRobot = []
		self.carte = carte
		self.begin = False

		print("map choisi :\n{}\n".format(self.carte.__str__()))

		print("setup the connexion ...")
		self.main_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.main_connexion.bind((hote, port))
		self.main_connexion.listen(5)

		print("done\n")
		print("listening on port : {}".format(port))

	def __del__(self):
		print("serveur will close")
		for client in self.lstClient:
			client.send("end".encode())
			client.close()
		print("all client connexion are now close")
		print("now close main connexion and exit")
		self.main_connexion.close()

	def getClient(self):
		"""
		function qui obtient les client avant le debut de la partie
		"""
		while self.begin is False:
			# regarde pour de nouvel connexion
			connexionW, _, _ = select.select([self.mainConnexion], [], [], 0.05)
			self.addClient(connexionW)

			connexionR = []
			try:
				connexionR, _, _ = select.select(self.lstClient, [], [], 0.05)
			except select.error:
				pass
			else:
				self.readClient(connexionR)

	def readClient(connexionRead):
		"""
		function qui lit les messages des clients
		"""
		for client in  connexionRead:
			msgRcv = client.recv(1024)
			msgRcv = msgRcv.decode()
			print("from client {} : {}".format(self.lstClient.index(client) + 1, msgRcv))
			if msgRcv in "c":
				if self.begin is False:
					self.begin = True
				else:
					client.send("la partie a deja commencer".encode())
			else:
				self.handle_msg(msgRcv, client)

	def addClient(self, connexionWanted):
		"""
		function qui ajoute les clients
		"""
		for conn in connexionWanted:
			connexion, info = conn.accept()
			print("client connected :", info)
			# ajoute le client a la liste
			self.lstClient.append(connexion)
			# on choisi une zone aleatoire
			x, y = self.carte.pickRandomLocation()
			# on creer le nouveau robot
			newRobot = Robot(x, y, "player".format(len(self.lstRobot) + 1))
			# on ajoute le robot a la liste
			self.lstRobot.append(newRobot)
			# on renvoie la map update a tout les clients
			self.reSendMap()
			# on envoie les infos au nouveau client
			msg = "votre robot : " + newRobot.__str__()
			connexion.send(msg.encode())

	def handle_msg(self, msg, client):
		"""
		gere les messages envoyer par les clients
		"""
		av = msg.split(' ')
		reg = r'^[nsewmp][0-9]*$'
		if av[0] in "/say":
			return self.sendMessageToAll(av, client)
		if av[0] in "/ls":
			pass
			# return self.sendListPlayer(client)
		if re.search(reg, av[0]):
			return client.send("you wanted to move".encode())
		msg = "{} command not found".format(msg)
		client.send(msg.encode())

	def sendMessageToAll(self, av, client):
		"""
		function qui envoie un message a tout les clients
		"""
		msg = ' '.join(av[1:])
		msg = "from Player {} :{}".format(lst_client.index(client) + 1, msg)
		msg = msg.encode()
		for c in self.lst_client:
			if c is not client:
				c.send(msg)

	def reSendMap(self):
		"""
		function qui renvoie la map a tout les clients
		"""
		for rob, cli in zip(self.lstRobot, self.lstClient):
			msg = self.addRobotToMap(rob)
			cli.send(msg.encode())

	def addRobotToMap(self, main_robot):
		"""
		function qui ajoute le robot a la map
		"""
		lab = self.carte.labyrinthe
		for robot in self.lstRobot:
			lab[robot.coord] = "x"
		lab[main_robot.coord] = "X"
		save = self.carte.labyrinthe
		self.carte.labyrinthe = lab
		chaine = self.carte.__str__()
		self.carte.labyrinthe = save
		return chaine
