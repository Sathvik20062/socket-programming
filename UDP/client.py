import socket
socketObject =socket.socket()
UDP_IP_ADDRESS = socket.gethostname()
UDP_PORT_NO = 1234
Message = "Hello, server ".encode()

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = str(input("Enter your Message:"))
    msg = msg.encode()
    
    
    clientSock.sendto(msg, (UDP_IP_ADDRESS,UDP_PORT_NO))