import socket

host = "localhost"
port = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4,tcp

s.bind((host, port))
print("Server listening on port ",port)
s.listen(1)

client, clientaddress = s.accept()

print("Connection Established to :", str(clientaddress))
client.send(b"From Server:Hi client How are you?")
client.send(b"From Server:Bye")
client.close()