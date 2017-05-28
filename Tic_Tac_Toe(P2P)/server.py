import tkinter as tk
import socket

class Conexão(object):
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

	def inicializar(self):
		self.conn = Conexão()
		self.conn.wait_message()
		#self.bd = BD()


root = tk.Tk()
root.title('Projeto Infracom(Server)')
#Os dois comando abaixo são usados para definir o tamanho da janela
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(700,500))
root.configure(background='black')

interface = GUI_Server(root)
interface.inicializar()
root.mainloop()
