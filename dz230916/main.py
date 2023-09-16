import random
import time
from threading import Thread


class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
        self.s = True

    def run(self):
        while self.s:
            time.sleep(1)

    def check(self):
        if self.is_alive():
            msg = "%s is working" % self.name
            print(msg)

    def stop(self):
        self.s = False

class ThredsHolder:
    def __init__(self):
        self.threads = dict.fromkeys(list(range(10)))

    def start(self, i):
        if i in self.threads.keys():
            t = MyThread(i)
            t.start()
            self.threads[i] = t

    def list(self):
        for i in self.threads.keys():
            if self.threads[i] != None:
                self.threads[i].check()

    def stop(self, i):
        if i in self.threads.keys():
            if self.threads[i] != None:
                self.threads[i].stop()





if __name__ == "__main__":
    TH = ThredsHolder()
    while True:
        s = input().split()
        if s[0] == "start":
            TH.start(int(s[1]))
        if s[0] == "list":
            TH.list()
        if s[0] == "stop":
            TH.stop(int(s[1]))
