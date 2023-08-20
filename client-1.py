import socket

print("Cliente")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
print("Host: ", host)
port = 9999

s.connect((host, port))
s.sendall(bytes("texto original", 'UTF-8'))

rec = s.recv(1024)

print("Recebido", rec.decode("utf-8"))

s.close()