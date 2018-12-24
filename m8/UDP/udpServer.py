import socket
def main():
    host = "10.10.8.239"
    port = 5053
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    print("server started")
    while True:
    	data, addr = s.recvfrom(1024)
    	data = data.decode()
    	if data == 'q':
    		break
    	print ("Message from " + str(addr))
    	print ("From connected user" + data)
    	data = str(data).upper()
    	print ("sending" + data)
    	s.sendto(data.encode(), addr)
    s.close()



if __name__ == '__main__':
	main()
