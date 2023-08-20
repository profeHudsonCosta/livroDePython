import socket
print("Servidor")

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = socket.gethostname()
print("Host = ", host)
port = 9999

serversocket.bind((host, port))
serversocket.listen(1)

while True:
    clientsocket, addr = serversocket.accept()
    recebido = clientsocket.recv(1024)
    if not recebido: break
    print(recebido)
    strRecebido = recebido.decode('UTF-8')
    print(str(host), ":", strRecebido)
    clientsocket.shutdown(socket.SHUT_RDWR)
    clientsocket.close()