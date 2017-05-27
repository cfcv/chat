import os
import commands
import socket
import threads


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Servidor criado"

host = raw_input('IP:')

try:
	port = int(raw_input('Port:'))
except ValueError:
	print "The port must be an integer\n"

server.bind((host,port))
server.listen(1)
while True:
	print "Waiting for connection\n"
	conection, client = server.accept()
	try:
		print "Get conection from ", client
	finally:
		while True:
			
		print "Connection closed"	
server.close()
print "Servidor fechado"
