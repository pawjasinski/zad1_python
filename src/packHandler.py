#!/usr/bin/env python3
import threading

class PackHandler(threading.Thread):
    def __init__(self):
        super().__init__()
        self.cond = threading.Condition()
        self.lst = []
    
    def add(self, nmb):
        with self.cond:
            self.lst.append(nmb)
            self.cond.notify()
    
    def pop(self):
        with self.cond:
            while len(self.lst) == 0:
                self.cond.wait()

            ret = self.lst[0]
            self.lst.pop(0)
            return ret
        
    def end(signum):
        self.cond.