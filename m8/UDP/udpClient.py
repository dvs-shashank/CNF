import socket
def main():
	host =  "10.10.8.239"
	port = 5052
	server = ('10.10.8.239', 5053)
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))
	message = input("Enter :    ")
	while message != 'q':
		s.sendto(message.encode(), server)
		data, addr = s.recvfrom(1024)
		data = data.decode()
		print ("received from server " +str(data))
		message = input("Enter :    ")
	s.sendto(b'q', server)
	s.close()


if __name__ == '__main__':
	main()

