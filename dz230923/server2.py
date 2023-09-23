import os
import socket
from threading import Thread

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65431  # Port to listen on (non-privileged ports are > 1023)

class ChatReaderThread(Thread):
    def __init__(self, conn, addr):
        """Инициализация потока"""
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.b = True

    def run(self):
        with self.conn:
            while self.b:
                try:
                    data = self.conn.recv(1024)
                    if data.decode('UTF-8') == "goodbye":
                        self.stop()
                    print(data.decode('UTF-8'))
                except ConnectionAbortedError:
                    break
    def stop(self):
        self.b = False

class ChatWriterThread(Thread):
    def __init__(self, conn, addr):
        """Инициализация потока"""
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.b = True

    def run(self):
        with self.conn:
            while self.b:
                data = input()
                if self.b:
                    self.conn.sendall(bytes(data, 'UTF-8'))
                    if data == "goodbye":
                        self.stop()
    def stop(self):
        self.b = False


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        crt = ChatReaderThread(conn, addr)
        cwt = ChatWriterThread(conn, addr)

        crt.start()
        cwt.start()

        while crt.b and cwt.b:
            pass

        crt.stop()
        cwt.stop()


if __name__ == "__main__":
    main()