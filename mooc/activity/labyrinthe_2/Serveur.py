from Class.Carte import Carte
from Class.Maps import Maps
from Class.Robot import Robot
from Class.Serveur import Serveur
import socket
import select
import utils
import os
import sys
import signal

# le repertoire ou se trouve les maps
dirToMap = "map"
# nom de l'hote
hote = ""
# port du serveur
port = 12800
# class serveur
sev = None

def sigint_handler(n, stack):
	for client in sev.lstClient:
		client.send("end".encode())
		client.close()
	sev.main_connexion.close()
	sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

"""
on choisi la map
"""
maps = Maps(dirToMap)
maps.readFromAgr()
carte = maps.getMapFromChoice()
del maps

sev = Serveur(carte, hote, prot)
del carte


print("now wait form client to connect ...")
begin_to_play = False
while begin_to_play == False:
	# on regarde si il y a des client qui se connect au serveur
	connexion_wanted, wlist, xlist = select.select([main_connexion], [], [], 0.05)

	for connexion in connexion_wanted:
		connexion_client, infos_connexion = connexion.accept()
		print("client connected :", infos_connexion)
		connected_client.append(connexion_client)
		# choisi une zone aleatoire
		x, y = carte.pickRandomLocation()
		# on creer un nouveau robot
		new_robot = Robot(x, y, "player".format(len(Robot_list)))
		# on ajoute le robot a la liste
		Robot_list.append(new_robot)
		# renvoie la map a tout client
		utils.reSendMap(Robot_list, connected_client, carte)
		# et envoie le nom du robot
		msg = "votre robot : " + new_robot.__str__()
		connexion_client.send(msg.encode())

	playerRead = []
	try:
		playerRead, wlist, xlist = select.select(connected_client, [], [], 0.05)
	except select.error:
		pass
	else:
		for client in playerRead:
			msg_rcv = client.recv(1024)
			msg_rcv = msg_rcv.decode()
			if msg_rcv in "c":
				begin_to_play = True
			else:
				print("from client {} : {}".format(connected_client.index(client) + 1, msg_rcv))
				utils.handle_msg(msg_rcv, client, connected_client)

print("serveur will close")
for client in connected_client:
	client.send("end".encode())
	client.close()
print("all client connexion close now close main connexion and exit")
main_connexion.close()
