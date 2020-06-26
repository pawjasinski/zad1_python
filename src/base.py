#!/usr/bin/env python3
import threading

class Base(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.isRun = True
    
    def end(signum):
        print("ending")
        self.isRun = False