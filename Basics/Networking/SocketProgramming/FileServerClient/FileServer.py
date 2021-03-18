import socket

host = "localhost"
port = 4001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
print("Server listening on port ", port)
s.listen(1)

clientconnection, clientaddress = s.accept()

print("Established connection with :", str(clientaddress))

filenamefromclient = clientconnection.recv(1024).decode()
try:
    f = open(filenamefromclient, 'rb')
    content = f.read()
    print("sending file ", filenamefromclient, " to client")
    clientconnection.send(content)
except FileNotFoundError:
    clientconnection.send(b"file not found")
finally:
    f.close()

s.close()
