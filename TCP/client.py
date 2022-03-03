import socket
socketObject = socket.socket()
socketObject.connect((socket.gethostname(),1234))
print("connected to",socket.gethostname())      
HTTPMessage="hello i am connected"
bytes=str.encode(HTTPMessage)
socketObject.sendall(bytes)
while(True):
    data=socketObject.recv(1024)
    print(data)
    if(data!=b''):
        HTTPMessage=input("Enter ur message:")
        bytes=str.encode(HTTPMessage)
        socketObject.sendall(bytes)
        if HTTPMessage=='q':
            print("connection closed")
            break
socketObject.close()