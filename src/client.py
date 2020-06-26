#!/usr/bin/env python3
import threading
from packHandler import *
import random
import time
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class Client(threading.Thread):
    def __init__(self, number):
        super().__init__()
        self.lst = []
        self.file = 'log' + str(number) + '.log'
        self.delay = 100 # 100 miliseconds
        self.isRun = True

    def registerHandler(self, PH):
        self.ph = PH

    def rand(self):
        random.seed(self)
        self.rnd = random.randint(0, 2500000000)
    
    def push(self):
        self.ph.add(self.rnd)
        self.lst.append(self.rnd)

    def saveLog(self):
        with open(self.file, 'w') as f:
            for line in self.lst:
                f.write(line)
    
    def receiveSig(self, sig):
        print('client rec sig: ' + sig)
        self.run = False
    
    def run(self):
        logging.debug('debug')
        while self.run:
            self.rand()
            self.push()
            time.sleep(self.delay/1000.)
        self.saveLog()

    def end(signum):
        print("client ending")
        self.isRun = False