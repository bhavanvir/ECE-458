import socket

UDP_IP = "134.87.191.64"
UDP_PORT = 8500

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data = sock.recvfrom(1024)
    print("recieved message " + data)
