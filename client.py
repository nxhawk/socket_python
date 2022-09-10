import socket

HOST = '127.0.0.1'
SERVER_PORT = 65432
FORMAT = 'utf8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('CLIENT SIDE')
client.connect((HOST, SERVER_PORT))
print('client address:', client.getsockname())


def sendList(client, list):
    for item in list:
        client.sendall(item.encode(FORMAT))
        client.recv(1024)

    msg = 'end'
    client.send(msg.encode(FORMAT))


def loginForm(client):
    username = input('username: ')
    client.sendall(username.encode(FORMAT))
    password = input('password: ')
    client.sendall(password.encode(FORMAT))

def registerForm(client):
    username = input('username: ')
    password = input('password: ')
    client.sendall(username.encode(FORMAT))
    client.sendall(password.encode(FORMAT))


list = ["hao1", "hao2", "hao3"]

try:
    msg = None
    while msg != 'x':
        msg = input('talk: ')
        client.sendall(msg.encode(FORMAT))
        if(msg == 'list'):
            sendList(client, list)
        if(msg == 'login'):
            loginForm(client)
        if(msg=='register'):
            registerForm(client)
except:
    print('error')

client.close()
