import socket

HOST = '127.0.0.1'
SERVER_ROOT = 65432
FORMAT = 'utf8'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SOCK_STREAM
s.bind((HOST, SERVER_ROOT))
s.listen()

print('SERVER SIDE')
print('server: ', HOST, SERVER_ROOT)
print('Waiting for Client')

conn, addr = s.accept()  # wait client connect
# conn nhan va trao doi duong truyen
# addr lay dia chi client

# with every client side
print('client address: ', addr)
print('conn:', conn.getsockname())

username = conn.recv(1024).decode(FORMAT)

print('username: ', username)
