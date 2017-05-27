import tkinter as tk
import socket

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
		self.frame1.pack()
		self.titulo.pack()

	def socket_server(self):
		self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		#Debug
		print("Server socket criated.")

		self.port = 5399
		self.ip = '127.0.0.1'
		self.server_socket.bind((self.ip,self.port))
		#Debug
		print("Escutando porta",self.port)
		print("Waiting for messagem")
		
		self.data, self.addr = self.server_socket.recvfrom(1024)
		if (len(self.data) > 0):
			print("mensagem: ",self.data)
			print("IP:",self.addr)

	def close_socket(self):
		self.server_socket.close()
		#Debug
		print("Socket closed.")
		#criando o banco de dados


root = tk.Tk()
root.title('Projeto Infracom(Server)')
#Os dois comando abaixo são usados para definir o tamanho da janela
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(700,500))
root.configure(background='black')
interface = GUI_Server(root)
interface.inicializar()
root.mainloop()
