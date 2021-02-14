#Created by Rsecurity

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(6)

host = input("Please enter the Ip to scan: ")
port = int(input("Please enter the port to scan: ")

def portScanner(port):
	if s.connect_ex((host, port)):
		print("The port is closed")
	else:
		print("The port's open")

portScanner(port)