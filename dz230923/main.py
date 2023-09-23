import socket

def f():
    HOST = "127.0.0.1"
    PORT = 65431


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    print(f"Received {data.decode('utf-8')}")

                    if data.decode('utf-8') == "goodbye":
                        conn.close()
                        return None

                    a = input()
                    conn.sendall(bytes(a, 'UTF-8'))

                    if a == "goodbye":
                        conn.close()
                        return None



f()