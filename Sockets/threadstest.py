import multiprocessing
import socket
from time import sleep


def envir(q):
    airspeed = 0
    alt = 0
    print(multiprocessing.Process.name)
    while True:
        airspeed += 2
        alt += 1
        q.put([airspeed, alt])


def try_con(ip, port, time=0, tries=5):
    for i in range(1, tries + 1):
        try:
            print('Connecting to {} at {}'.format(ip, port))
            s.connect((ip, port))
            return
        except:
            time += 2
            print('Failed try {} out of {} , trying again in {} seconds'.format(i, tries, time))
            sleep(time)


o = 0
s = socket.socket()
# Setup Socket
try_con('127.0.0.1', 8889)
print('Connection Successful')

while 1:
    print(s.recv(1024))

'''
if __name__ == '__main__':
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=envir, args=(q,))
    p.start()
    while True:
        for p in range(0, len(q.get()) - 1):
            val = q.get()
            s.send(bytes(str([val[p], val[p - 1]]), 'UTF-8'))
    p.join()
    s.close()
'''
