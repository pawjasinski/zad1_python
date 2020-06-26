#!/usr/bin/env
import threading

class Watcher(threading.Thread):
    def __init__(self):
        super().__init__()
        self.watchedList = []
        self.isRun = True

    def registerWatched(self, W):
        self.watchedList.append(W)