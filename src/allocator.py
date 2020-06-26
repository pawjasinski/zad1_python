#!/usr/bin/env python3
import threading

class Allocator(threading.Thread):
    def __init__(self):
        super().__init__()
        #self.run = True
        self.lck = threading.Lock()

    def getString(self, nmb):
        with self.lck:
            return str(nmb)

    #def receiveSig(self, sig):
    #    print('Allocator rec sig: ' + sig)
    #    self.run = False