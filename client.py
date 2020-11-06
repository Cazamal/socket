

import socket
host = "127.0.0.1"
port = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
while True:
    msg = input("Digite uma mensagem")
    s.sendall(str.encode(msg))
    data = s.recv(1024)
    print("Você digitou :", data.decode())
    if not msg:
        print("Desconectado")
        break