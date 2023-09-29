import os
import socket
from threading import Thread

HOST = "127.0.0.1"
PORT = 65431

class ChatReaderThread(Thread):
    def __init__(self, s):
        """Инициализация потока"""
        Thread.__init__(self)
        self.s = s
        self.b = True

    def run(self):
        with self.s:
            while self.b:
                try:
                    data = self.s.recv(1024)
                    print(data.decode('UTF-8'))
                except ConnectionAbortedError:
                    break

    def stop(self):
        self.b = False

class ChatWriterThread(Thread):
    def __init__(self, s):
        """Инициализация потока"""
        Thread.__init__(self)
        self.s = s
        self.b = True

    def run(self):
        with self.s:
            while self.b:
                data = input()
                if self.b:
                    self.s.sendall(bytes(data, 'UTF-8'))
                    if data == "goodbye":
                        self.stop()
    def stop(self):
        self.b = False


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        crt = ChatReaderThread(s)
        cwt = ChatWriterThread(s)
        crt.start()
        cwt.start()
        while crt.b and cwt.b:
            pass

        crt.stop()
        cwt.stop()



if __name__ == "__main__":
    main()