from http import client
import socket

HOST = '127.0.0.1'
SERVER_PORT = 65432
FORMAT = 'utf8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('CLIENT SIDE')
client.connect((HOST, SERVER_PORT))
print('client address:', client.getsockname())


username = input("username: ")

client.sendall(username.encode(FORMAT))
# gui du lien bind du lieu khi gui
