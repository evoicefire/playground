import socket
from time import sleep


def try_con(ip, port, time=0, tries=5):
    for i in range(1, tries + 1):
        try:
            s.connect((ip, port))
            return
        except:
            time += 2
            print('Failed try {} out of {} , trying again in {} seconds'.format(i, tries, time))
            sleep(time)
    exit()

# Setup Socket
s = socket.socket()
ip = input('IP?')
port = int(input('Port?'))
print('Trying to Connect')
try_con(ip, port)
print('Connected!')
while 1:
    s = socket.socket()
    try:
        try_con(ip, port)
    except socket.error:
        print('Lost connection to server. Bad network?')
    s.send(bytes(input(), 'UTF-8'))
    s.close()

