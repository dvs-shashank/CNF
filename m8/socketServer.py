import socket
def main():
	host = "10.10.8.239"
	port = 5050
	s = socket.socket()
	s.bind((host, port))
	s.listen(1)
	c, addr = s.accept()
	# print "bbkjbk"
	print ("Connection from" + str(addr))
	while True:
		data = c.recv(1024).decode()
		# data.decode()
		if not data:
			break;
		print ("from connected user" + str(data))
		data = str(data).upper()
		print ("Sending" + str(data))
		c.send(data.encode())
	c.close()
if __name__ == '__main__':
    main()

