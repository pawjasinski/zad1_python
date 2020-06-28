#!/usr/bin/env python3
from zadLoger import *
import threading

class Allocator():
    def __init__(self):
        self.lck = threading.Lock()
    
    def toString(self, i: int) -> int:
        with self.lck:
            return str(i)