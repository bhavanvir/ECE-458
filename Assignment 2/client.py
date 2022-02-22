import socket

UDP_IP = "134.87.141.252"
UDP_PORT = 8500

while True:
    message = bytes(input(), "utf-8")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.sendto(message, (UDP_IP, UDP_PORT))