"""

Server

Author: George Macrae
2014

"""


from socket import *
import threading
import sys

def handler(clientsocket, clientaddr):
    print "Accepted connection from: ", clientaddr
    clients.append(clientsocket)
    while 1:

        data = clientsocket.recv(1024)
        if data == 'Exit':
            clientsocket.send('Exit')
            clients.remove(clientsocket)
            break

        for x in clients:
            if x != clientsocket:
                x.send(data)
          

 
if __name__ == "__main__":
 
    host = gethostbyname(gethostname())
    port = 9999
    addr = (host, port)
 
    serversocket = socket(AF_INET, SOCK_STREAM)
 
    serversocket.bind(addr)
 
    serversocket.listen(2)
 
    print host
    
    global clients
    clients = []
    while 1:
        print "Server is listening for connections\n"
 
        clientsocket, clientaddr = serversocket.accept()
        h_thread = threading.Thread(target = handler, args = (clientsocket, clientaddr))
        h_thread.start()
