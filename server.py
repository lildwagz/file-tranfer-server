
import socket
import threading
import os

def menerima(name, socket):
    filename = socket.recv(1024)
    if os.path.isfile(filename):
        socket.send("EXISTS " + str(os.path.getsize(filename)))
        userResponse = socket.recv(1024)
        if userResponse[:2] == 'OK':
            with open(filename, 'rb') as f:
                bytesToSend = f.read(1024)
                socket.send(bytesToSend)
                while bytesToSend != "":
                    bytesToSend = f.read(1024)
                    socket.send(bytesToSend)
    else:
        socket.send("ERR ")

    socket.close()

def Main():
    host = '127.0.0.1'
    port = 2112


    s = socket.socket()
    s.bind((host,port))

    s.listen(5)

    print "Server sudah siap."
    while True:
        c, addr = s.accept()
        print "client baru dari :<" + str(addr) + ">"
        t = threading.Thread(target=menerima, args=("RetrThread", c))
        t.start()
         
    s.close()

if __name__ == '__main__':
    Main()
