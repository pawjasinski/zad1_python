#!/usr/bin/env python3
from zadLoger import *
import threading

class PackHandler():
    def __init__(self):
        self.lst = []
        self.lck = threading.Lock()
        self.cond = threading.Condition(self.lck)
    
    def add(self, random: int):
        with(self.cond):
            self.lst.append(random)
            self.cond.notify()
    
    def get(self) -> int:
        while len(self.lst) == 0:
            self.cond.wait()
        
        ret = self.lst[0]
        self.lst.pop(0)
        return ret