import socket

def main():
	host = '10.10.8.239'
	port = 3600

	s = socket.socket()
	s.connect((host,port))
	print("welcome to guess my number: ")
	message = input("Enter your guess: ")
	while True:
		s.send(message.encode())
		data = s.recv(1024).decode()
		print(str(data))
		num = str(data).split(':')
		if len(num) == 2:
			break
		message = input("Enter your guess: ")
		
	s.close()
if __name__ == "__main__":
	main()	