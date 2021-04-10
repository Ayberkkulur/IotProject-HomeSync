import socket
import time



HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print( "Bind failed", msg[0], msg[1])
    sys.exit()

s.listen(1)
print("Waiting for a connecting client...")
isConnected = False
conn, addr = s.accept()
print("Connected with client at " + addr[0])
isConnected = True



while True:
    # receive data stream. it won't accept data packet greater than 1024 bytes
    data = conn.recv(1024).decode()
    print("from connected user: " + str(data))
    



