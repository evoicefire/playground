import socket
import sys

__author__ = 'Gus'

HOST = ''
PORT = 8889

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print('Socket bind complete')

s.listen(10)
print('Socket now listening')

while 1:
    conn, addr = s.accept()
    print('Connection get {}'.format(addr))
    while True:
        print(conn.recv(1024))
s.close()
