import socket
import sys

__author__ = 'Gus'

HOST = ''
PORT = 8889

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('--Socket created--')

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print('Bound')

s.listen(10)
print('Listening')
conn, addr = s.accept()
print('Connection get {}'.format(addr))
while 1:
    conn, addr = s.accept()
    try:
        string = conn.recv(1024).decode("UTF-8")
    except (UnicodeDecodeError, ConnectionResetError):
        try:
            string = conn.recv(1024)
        except ConnectionResetError:
            print('Connection Reset')
            string = ''
            pass
    print(string)
    conn.close()

