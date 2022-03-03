import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_add=socket.gethostname()
port=1234
serversocket.bind((ip_add,port))
print("Server socket bound with ip_add {} port{}". format(ip_add,port))
serversocket.listen()
while True:
    connection, client_address = serversocket.accept()
    print("Client connected", client_address, connection)
    while(True):
        data=connection.recv(1024)
        print(data)
        if(data!=b''):
            msg1=input("enter your message")
            msg1Bytes=str.encode(msg1)
            connection.send(msg1Bytes)
            if msg1=='q':
                print("connection closed")
                break
        