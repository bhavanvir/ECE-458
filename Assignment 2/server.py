import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket created: ", s)

s.bind(('127.0.0.1', 9300))
s.listen()

print("Waiting for connections...")

while True:
    c, addr = s.accept()
    print("Connected with: ", addr)

    userInput = c.recv(1024).decode()

    inputList = userInput.split(' ')

    inputList = [int(i) for i in inputList]

    listLength = len(inputList)
    if(listLength < 5 or listLength > 5):
        c.send(bytes(f'Numbers entered: {listLength}, numbers expected: 5', 'utf-8'))
    else:
        inputList.sort()

        c.send(bytes(f'Smallest value: {inputList[0]}, largest value: {inputList[4]}', 'utf-8'))

    c.close()

