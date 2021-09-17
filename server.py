import socket

s = socket.socket()
print('socket created')

s.bind(("localhost", 9999))

s.listen(3)
print('waiting for connection')

# while True:
c, addr = s.accept()
name = c.recv(1024).decode()
print("connected with", addr, name)
c.send(bytes("welcome to chat", "utf-8"))
while True:
    message = input('Me : ')
    c.send(message.encode())
    message = c.recv(1024)
    message = message.decode()
    print(name, ':', message)

# c.close()
