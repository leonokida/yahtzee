import socket

IP = "127.0.0.1"
PORT = 5000

ME = "A"
ADDREC = 5003
ADDSEND = 5001

relayBaton = True

mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mySocket.bind((IP, PORT))

while True:
    if relayBaton:
        print("Tenho bastão")
        input()
        mySocket.sendto(b"bastao", (IP, ADDSEND))
        relayBaton = False
    else:
        data, addr = mySocket.recvfrom(1024)
        if addr[1] == ADDREC:
            if data == b'bastao':
                relayBaton = True