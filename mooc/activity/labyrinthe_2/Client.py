import time
import socket
import select
import sys
import utils
import signal
import os
from threading import RLock
from Class.Client import ReadInput, SendInput

hote = "localhost"
port = 12800

client_connexion = None
readinTh = None

verrouDisplay = RLock()

print("=================================================")
print("  welcome")
print("    commande :")
print("      /say [message] : send message to all player")
print("  hote :", hote)
print("  port :", port)
print("=================================================")

def handler_sigint(n, stack):
	if readingTh is not None:
		readingTh.stop()
		readingTh.join()
	if client_connexion is not None:
		client_connexion.close()
	sys.exit(0)

signal.signal(signal.SIGINT, handler_sigint)

client_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("try to connect to {}".format((hote, port)))
client_connexion.connect((hote, port))
print("done\n")

print(client_connexion.recv(1024).decode())

readingTh = ReadInput(client_connexion, verrouDisplay)
readingTh.daemon = True
readingTh.start()

"""
read input from user
"""
print(">> ", end='')
while True:
	msg = input("")
	client_connexion.send(msg.encode())

readingTh.join()
client_connexion.close()
