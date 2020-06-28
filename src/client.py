#!/usr/bin/env python3
from packHandler import *
from zadLoger import *
import random

class Client():
    def __init__(self, number):
        self.id = number
        self.lst = []
        self.file = 'log' + str(number) + '.log'
        random.seed(self.id)

    def registerHandler(self, PH):
        self.ph = PH

    def rand(self):
        self.rnd = random.randint(0, 2500000000)
    
    def push(self):
        self.ph.add(self.rnd)
        self.lst.append(self.rnd)

    def saveLog(self):
        with open(self.file, 'w') as f:
            for line in self.lst:
                f.write(str(line))