import socket

host = "localhost"
port = 4001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

filename = input("Enter file name:")

s.send(filename.encode())

filecontentfromserver = s.recv(1024)

print(filecontentfromserver.decode())

s.close()

