from threading import Thread, RLock, Event
import socket
import select
import signal
import os
import sys

ingame = True

class ReadInput(Thread):

	def __init__(self, connexion, verrouDisplay):
		Thread.__init__(self)
		self.connexion = connexion
		self.displayLock = verrouDisplay
		self.loop = True

	def run(self):
		while self.loop is True:
			msgFromServeur, wlist, xlist = select.select([self.connexion], [], [], 0.05)
			for msgServeur in msgFromServeur:
				msg = msgServeur.recv(1024)
				msg = msg.decode()
				if msg in "end":
					os.kill(os.getpid(), signal.SIGINT)
					break
				else:
					with self.displayLock:
						print("\n{}".format(msg))
						print(">> ", end='')
						sys.stdout.flush()

	def stop(self):
		self.loop = False

class SendInput(Thread):

	def __init__(self, socket):
		Thread.__init__(self)
		self.stop = Event()
		self.connexion = Connection()
		self.socket = socket

	def run(self):
		global ingame
		run = True
		while run is True or self.stop.is_set() is False:
			try:
				print(">> ", end='')
				msg = sys.stdin.readline().strip()
				if msg:
					self.socket.send(msg.encode())
			except CommunicationException:
				pass
			with verrouGame:
				run = ingame

		def terminate(self):
			self.stop.set()
			self.connexion.close()
