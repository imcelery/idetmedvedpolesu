import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65431  # The port used by the server

def f():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            a = input()

            s.sendall(bytes(a, 'UTF-8'))

            if a == "goodbye":
                s.close()
                return None

            data = s.recv(1024)
            print(f"Received {data.decode('utf-8')}")

            if data.decode('utf-8') == "goodbye":
                s.close()
                return None

f()