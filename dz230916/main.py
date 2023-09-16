import random
import time
from threading import Thread


class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
        self.s = True

    def run(self):
        if s:
            amount = random.randint(5, 6)
            time.sleep(amount)
        if s:
            msg = "%s ВЫПОЛНИЛ ПРИКАЗ" % self.name
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

    def status(self, i):
        if i in self.threads.keys():
            if self.threads[i] != None:
                if self.threads[i].is_alive():
                    print(f"Поток {i} ЖИВ")
                else:
                    print(f"Поток {i} УМЕР")
            else:
                print(f"Поток {i} И НЕ ЖИЛ ВОВСЕ")

    def stop(self, i):
        if i in self.threads.keys():
            if self.threads[i] != None:
                if self.threads[i].is_alive():
                    self.threads[i].stop()
                    print(f"Поток {i} УБИЛИ")
            else:
                print(f"Поток {i} И НЕ ЖИЛ ВОВСЕ")




if __name__ == "__main__":
    TH = ThredsHolder()
    while True:
        s = input().split()
        if s[0] == "start":
            TH.start(int(s[1]))
        if s[0] == "status":
            TH.status(int(s[1]))
        if s[0] == "stop":
            TH.stop(int(s[1]))
