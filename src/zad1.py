#!/usr/bin/env python3
from client import *
from server import *
from allocator import *
from packHandler import *
from watcher import *
import signal
import logging
import base

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

isRun = True

def sigHandler(signum, frame):
    isRun = False

if __name__ == '__main__':
    #signal.sigal(signal.SIGINT, sigHandler)

    Th = PackHandler()

    T1 = Client(1) # Client thread
    T1.registerHandler(Th)

    T2 = Client(2)
    T2.registerHandler(Th)
    
    T3 = Client(3)
    T3.registerHandler(Th)
    
    T4 = Server() # Server thread
    T4.registerHandler(Th)

    T5 = Server() 
    T5.registerHandler(Th)

    T6 = Allocator() # Allocator thread
    T4.registerAlloc(T6)
    T5.registerAlloc(T6)

    T7 = Watcher() # Watchdog thread
    T7.registerWatched(T4)
    T7.registerWatched(T5)

    threads = [ T1, T2, T3, T4, T5, T7]

    for t in threads:
        t.start()
    
    for t in threads:
        t.join()

    while isRun:
        time.sleep(1)