import tkinter as tk
import socket
import sqlite3

class DataBase(object):
	def __init__(self):
		self.conn = sqlite3.connect('users.db')
		self.cur = self.conn.cursor()
		self.cur.executescript('''
			DROP TABLE IF EXISTS Users;
			CREATE TABLE Users(
				login PRIMARY KEY,
				password VARCHAR(20),
				victory INTEGER,
				tie     INTEGER,
				loss    INTEGER);''')

#-----------------------------------------
class Conexão_Server(object):
	"""docstring for Conexão"""
	def __init__(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.port = 5399
		self.ip = '127.0.0.1'
		self.sock.bind((self.ip,self.port))
		#Debug
		print("Server socket created.")
		print("Escutando porta",self.port)
		print("Waiting for messagem")
		
	def send(self,mss):
		#Debug
		print("Enviando mensagem:",mss)
		self.sock.sendto(mss.encode(), (self.ip,self.port))

	def wait_message(self):
		while True:
			self.data, self.addr = self.sock.recvfrom(1024)
			if(len(self.data) > 0):
				print("Mensagem: ", self.data)
				print("From: ", self.addr)
#-----------------------------------------

class GUI_Server(object):
	"""docstring for GUI_Server"""
	def __init__(self, master):
		#---- Frames ----
		self.frame1 = tk.Frame(master)
		self.frame2 = tk.Frame(master)

		#---- Labels ----
		self.titulo = tk.Label(self.frame1,text='Servidor', bg='black', fg='red', font=("times",32,"bold italic"), height=5)
		
		#Debug
		print("Server is running")		
#-----------------------------------------

class Servidor(object):

	def __init__(self, master):
		self.connection = Conexão_Server()
		self.interface = GUI_Server(master)
		self.DB = DataBase()
		self.connection.wait_message()

		

root = tk.Tk()
root.title('Projeto Infracom(Server)')
#Os dois comando abaixo são usados para definir o tamanho da janela
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(700,500))
root.configure(background='black')

interface = Servidor(root)
root.mainloop()


