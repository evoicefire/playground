import socket
import sys
from time import sleep

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
param = [1, 2]
while 1:
    conn, addr = s.accept()

    print('Connection get {}'.format(addr))
    sleep(5)
    while True:
        for p in range(0, (len(param) - 1)):
            s.send(bytes(str([param[p], param[p - 1]]), 'UTF-8'))
s.close()
