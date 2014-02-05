"""
Client

Author: George Macrae
2014

"""

from socket import *
import threading
import sys
 
def listner(clientsocket):
	while True:
		data = clientsocket.recv(1024)
		if data == 'Exit':
			clientsocket.close()
			break
		dataL = data.split(':')


		name = dataL[1]
		msg = dataL[0]
		print "\n"+name +" says: "+ msg + "\n"


def writer(clientsocket):
	while True:
		data = raw_input()
		print "You say :"+ data
		clientsocket.send(data+":"+name)
		if not data:
			clientsocket.send('Exit')
			print "exiting..."
			break		


if __name__ == '__main__':
	global name
	name = raw_input('Enter your name:')
 	looper = True
 	host = gethostbyname(gethostname())
 	port = 9999
 	addr = (host, port)
 	clientsocket = socket(AF_INET, SOCK_STREAM)
 	clientsocket.connect(addr)
 	w_thread = threading.Thread(target = listner, args = (clientsocket,))
 	r_thread = threading.Thread(target = writer, args = (clientsocket,))
 	w_thread.start()
 	r_thread.start()
