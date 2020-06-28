#!/usr/bin/env python3

from client import *
from server import *
from allocator import *
from packHandler import *
from watcher import *
from zadLoger import *
import signal
import threading
import time

isRun = True

def client(id, t):
    cl = Client(id)
    cl.registerHandler(t)
    while isRun:
        cl.rand()
        cl.push()
        time.sleep(0.5)
    cl.saveLog()

def server(id, t, wt, al):
    srv = Server()
    srv.registerHandler(t)
    srv.registerAllocator(al)
    wt.registWatched(srv)
    while isRun:
        srv.pullrand()
        srv.intToString()
        srv.show()

def alocator(allctr):
    while isRun:
        allctr.ToString()


def watcher(wt):
    while isRun:
        srvref = wt.checkInactive()
        if srvref != None:
            srvref.reset()
            time.sleep(1)

if __name__ == '__main__':
    signal = signal.signal()

    al = Allocator()
    wtch = Watcher()
    th = PackHandler()
    
    threads = [
        threading.Thread(target = client, args = (1, th)),
        threading.Thread(target = client, args = (2, th)),
        threading.Thread(target = client, args = (3, th)),
        threading.Thread(target = server, args = (1, th, wtch, al)),
        threading.Thread(target = server, args = (2, th, wtch, al)),
        threading.Thread(target = alocator, args = (al,)),
        threading.Thread(target = watcher, args = (wtch,))
        ]
    
    for t in threads:
        t.join()