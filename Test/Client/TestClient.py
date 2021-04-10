import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432  # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(b'Hello, world')

while True:
    # receive data stream. it won't accept data packet greater than 1024 bytes
    data = s.recv(1024).decode()
    if not data:
        # if data is not received break
        break
    print("from connected user: " + str(data))
    data = input(' -> ')
    s.send(data.encode())




#data = s.recv(1024)

#print('Received', repr(data))