#!/usr/bin/env
from zadLoger import *

class Watcher(threading.Thread):
    def __init__(self):
        super().__init__()
        self.watchedList = []

    def registerWatched(self, w):
        self.watchedList.append(w)