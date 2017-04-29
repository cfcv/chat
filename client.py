import socket

def menu():
	"Function that prints the menu"
	print "------------------"
	print "1. Send Message"
	print "2. Read Message"
	print "3. Close connection"
	print "------------------"
	return int(raw_input('input:'))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = raw_input('IP to connect:')
try:
	port = int(raw_input('Port:'))
except ValueError:
	print "The port must be a number\n"

	
client.connect((host,port))

while True:
	choice = menu()
	if (choice < 4 and choice > 0):
		if(choice == 1):
			print "you choose send message\n"
			msg2 = raw_input('you: ')
			client.send(msg2)
		elif(choice == 2):
			print "you choose read message\n"
			while True:
				msg = client.recv(1064)
				if (len(msg) > 0):
					print msg
					break
		else:
			print "you choose close connection\n"
			break
	else:
		print "Wrong choose, try again\n"
client.close()