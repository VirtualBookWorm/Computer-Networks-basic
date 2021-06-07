import socket

myIP = socket.gethostbyname(socket.gethostname())
PORT = 32001
FORMAT = "utf-8"
ADDR = (myIP, PORT)

CLIENT = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
CLIENT.settimeout(3)

while True:
    data = input("Enter the text >> ")
    CLIENT.sendto(data.encode(FORMAT), ADDR)
    if data == 'close()':
        exit(0)
    else:
        data, addr = CLIENT.recvfrom(2048)
        text = data.decode(FORMAT)
        print("Received from server %s : %s" %(addr, text))



