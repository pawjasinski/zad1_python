#!/usr/bin/env python3
import threading
import time
from packHandler import *
from zadLoger import *


class Server():
    def __init__(self):
        self.lck = threading.Lock()

    def registerHandler(self, PH):
        self.ph = PH

    def registerAllocator(self, al):
        self.allctr = al
    
    def pullrand(self):
        self.lck.acquire()
        self.rand = self.ph.get()
        self.lck.release()

        while self.rand < 100000000 & self.rand > 0:
            time.sleep(0.100)
    
    def intToString(self):
        self.str = self.allctr.toString(self.rand)
    
    def show(self):
        print(self.str)

    def reset(self):
        with self.lck:
            self.rand = self.ph.get()