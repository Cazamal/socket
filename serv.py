
import socket 
host = 'localhost'
port = 50000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen()
print("Aguardando conexão do cliente...")
conn ,ender = s.accept()

print("Conectado em ", ender)
while True:
    data = conn.recv(1024)
    if not data:
        print("fechando a conexão")
        conn.close()
        break
    print(data)
    conn.sendall(data)
