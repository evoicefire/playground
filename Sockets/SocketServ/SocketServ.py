import socket
import sys

__author__ = 'Gus'

HOST = ''
PORT = 8889
p = 0
e = 0
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
    if p > 0:
        conn, addr = s.accept()
        if e == 0:
            print('Connection get {}'.format(addr))
    try:
        string = conn.recv(1024).decode("UTF-8")
        e += 1
        print(string)
    except:
        try:
            try:
                while 1:
                    string = conn.recv(4096).decode()
                    print(string)
            except:
                print('And unknown error occurred, lost client?')
                pass
        except ConnectionResetError:
            print('Connection Reset')
            e = 0
            p = 0
            string = ''
            pass
    conn.close()
    p += 1

