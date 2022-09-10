import socket
import threading
import json
# {}[]


def recieveList(conn):
    list = []
    item = conn.recv(1024).decode(FORMAT)

    while (item != 'end'):
        list.append(item)
        # response
        conn.sendall(item.encode(FORMAT))
        item = conn.recv(1024).decode(FORMAT)

    return list


def handleLogin(conn):
    username = conn.recv(1024).decode(FORMAT)
    print('username: ', username)
    password = conn.recv(1024).decode(FORMAT)
    print('password: ', password)
    with open('data.json', 'r') as f:
        data_list = json.load(f)
        if(username in data_list['Account']):
            index = data_list['Account'].index(username)
            if(password != data_list['Pass'][index]):
                print('wrong password')
            else:
                print('login successfully!!')
        else:
            print('no username')


def handleRegister(conn):
    username = conn.recv(1024).decode(FORMAT)
    password = conn.recv(1024).decode(FORMAT)
    with open('data.json', 'r+') as f:
        data_json = json.load(f)
        data_json['Account'].append(username)
        data_json['Pass'].append(password)
        f.seek(0)
        json.dump(data_json, f, indent=4)
        print('Added user')


def handleClient(conn, addr):
    # with every client side
    print('client address: ', addr)
    print('conn:', conn.getsockname())
    # []

    msg = 'none'
    while msg != 'x':
        msg = conn.recv(1024).decode(FORMAT)
        print('client', addr, 'says', msg)
        if(msg == 'list'):
            print('list: ', recieveList(conn))
        if(msg == 'login'):
            handleLogin(conn)
        if(msg == 'register'):
            handleRegister(conn)

    print('client', addr, 'finished, closed')
    conn.close()


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

nClient = 0
while nClient < 3:

    try:
        conn, addr = s.accept()  # wait client connect
        # conn nhan va trao doi duong truyen
        # addr lay dia chi client
        thr = threading.Thread(target=handleClient, args=(conn, addr))
        thr.daemon = True  # kill thr
        thr.start()

    except socket.error as err:
        print('error', err)

    nClient += 1


s.close()
