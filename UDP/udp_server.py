import socket

myIP = socket.gethostbyname(socket.gethostname())
PORT = 32001
FORMAT = "utf-8"
ADDR = (myIP, PORT)

SERVER = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
SERVER.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
SERVER.bind(ADDR)
print("Listening at {}".format(SERVER.getsockname()))

while True:
    msg_bytes, addr = SERVER.recvfrom(1024)
    msg_str = msg_bytes.decode(FORMAT)
    if msg_str == 'close()':
        exit(0)
    else:
        print("Received from client {} : {}".format(addr, msg_str))
        txt = msg_str.upper()
        SERVER.sendto(txt.encode(FORMAT), addr)

