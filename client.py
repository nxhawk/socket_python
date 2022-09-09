import socket

HOST = '127.0.0.1'
SERVER_PORT = 65432
FORMAT = 'utf8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('CLIENT SIDE')
client.connect((HOST, SERVER_PORT))
print('client address:', client.getsockname())


try:
    msg = None
    while msg != 'x':
        msg = input('talk: ')
        client.sendall(msg.encode(FORMAT))
        msg = client.recv(1024).decode(FORMAT)
        print('Server say: ', msg)

except:
    print('error')

client.close()
