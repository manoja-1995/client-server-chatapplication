import socket

c = socket.socket()

c.connect(('localhost', 9999))

name = input("Enter the name")

c.send(bytes(name, "utf-8"))

print(c.recv(1024).decode())
while True:
    message = (c.recv(1024)).decode()
    print(name, ":", message)
    message = input("Me : ")
    c.send(message.encode())



