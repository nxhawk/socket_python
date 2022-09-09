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
# []


def recieveList(conn):
    list = []
    item = conn.recv(1024).decode(FORMAT)

    while (item != 'end'):
        list.append(item)
        # response
        conn.sendall(item.encode(FORMAT))
        item = conn.recv(1024).decode(FORMAT)

    return list


try:

    msg = 'none'
    while msg != 'x':
        msg = conn.recv(1024).decode(FORMAT)
        print('client', addr, 'says', msg)
        if(msg == 'list'):
            print('list: ', recieveList(conn))

except:

    print('error')
