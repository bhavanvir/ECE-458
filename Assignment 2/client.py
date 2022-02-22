import socket

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

c.connect(("127.0.0.1", 9300))

userInput = input("Enter 5 numbers separated by spaces: ")

c.send(bytes(userInput,'utf-8'))

print(c.recv(1024).decode())