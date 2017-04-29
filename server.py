import os
import commands
import socket

def menu():
	"Function that prints the menu"
	print "------------------"
	print "1. Send Message"
	print "2. Read Message"
	print "3. Close connection"
	print "------------------"
	return int(raw_input('input:'))

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
			choice = menu()
			if(choice < 4 and choice > 0):
				if(choice == 1):
					print "you choose send message\n"
					os.system("clear")
					string = raw_input('you:')
					conection.send(string)
				elif(choice == 2):
					print "you choose read message\n"
					while True:
						msg = conection.recv(1064)
						if (len(msg) > 0):
							print "client:",msg
							break
				else:
					print "you choose close connection\n"
					break
			else:
				print "wrong choose, try again\n"
				continue

		print "Connection closed"	
server.close()
print "Servidor fechado"
