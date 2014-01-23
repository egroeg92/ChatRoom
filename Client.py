"""
Client

Author: George Macrae
2014

"""

from socket import *
import threading
import sys
 
def listner(clientsocket):
	while 1:
		data = clientsocket.recv(1024)
		if not data:
			clientsocket.close()			
			sys.exit()
		else:
			name = data.split("_")[0]
			msg = data.split("_")[1]
			print "\n"+name +" says: "+ msg + "\n$: "

def writer(clientsocket):
	while 1:
		data = raw_input("$: ")
		clientsocket.send(data)
		if not data:
			print "exiting..."			
			sys.exit()


if __name__ == '__main__':
 
    host = gethostbyname(gethostname())
    port = 9999

    addr = (host, port)
 
    clientsocket = socket(AF_INET, SOCK_STREAM)
 
    clientsocket.connect(addr)
    w_thread = threading.Thread(target = listner, args = (clientsocket,))
    r_thread = threading.Thread(target = writer, args = (clientsocket,))
    w_thread.start()
    r_thread.start()
