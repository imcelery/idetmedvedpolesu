import os
import socket
from threading import Thread

HOST = "127.0.0.1"
PORT = 65431

class ChatReaderThread(Thread):
    def __init__(self, conn, addr):
        """Инициализация потока"""
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.b = True
        self.message = None

    def run(self):
        with self.conn:
            while self.b:
                try:
                    data = self.conn.recv(1024)
                    if data.decode('UTF-8') == "goodbye":
                        self.stop()
                    self.message = data.decode('UTF-8')
                except ConnectionAbortedError:
                    break
    def stop(self):
        self.b = False

    def getMessage(self):
        if self.is_alive():
            if self.message != None:
                s = self.message
                self.message = None
                return s
            return None
        return False

    def write(self, message):
        self.conn.sendall(bytes(str(self.addr[0]) + " " + str(self.addr[1]) + " " + message, 'UTF-8'))

class ChatMeneger(Thread):
    def __init__(self):
        """Инициализация потока"""
        Thread.__init__(self)
        self.b = True
        self.threadList = []

    def run(self):
        while self.b:
            for i in self.threadList:
                message = i.getMessage()
                if message is not None:
                    if not message:
                        self.threadList.remove(i)
                    else:
                        for j in self.threadList:
                            if i != j:
                                j.write(message)

    def stop(self):
        self.b = False

    def addThread(self, th):
        self.threadList.append(th)


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        chM = ChatMeneger()
        chM.start()

        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            crt = ChatReaderThread(conn, addr)
            crt.start()

            chM.addThread(crt)

if __name__ == "__main__":
    main()