import  socket

host = "localhost"
port = 4000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

msg=s.recv(1024)

while msg:
    print("Message received from server:",msg.decode())
    msg=s.recv(1024)

s.close()