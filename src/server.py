#!/usr/bin/env python3
import threading
from packHandler import *
import logging
import base

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class Server(threading.Thread):
    def __init__(self):
        super().__init__()
        self.isRun = True
    
    def registerHandler(self, PH):
        self.ph = PH
    
    def registerAlloc(self, AL):
        self.al = AL

    def getRnd(self):
        self.rnd = self.ph.pop()
    
    def intToString(self):
        self.rndStr = self.al.getString(self.rnd)
    
    def print(self):
        print(self.rndStr)

    def receiveSig(self, sig):
        print('server rec sig: ' + sig)
        self.run = False

    def run(self):
        while self.run:
            self.getRnd()
            self.intToString()
            self.print()
    
    def end(signum):
        print("serverending")
        self.isRun = False