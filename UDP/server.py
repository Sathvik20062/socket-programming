import socket
UDP_IP_ADDRESS = socket.gethostname()
UDP_PORT_NO =1234
serversock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serversock.bind((UDP_IP_ADDRESS,UDP_PORT_NO))

while True:
    data, addr = serversock.recvfrom(1024)
    print ("Message: " + data.decode())