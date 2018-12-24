import socket
import threading 
import random
def main():
	host = '10.10.8.239'
	port = 3600

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host,port))
	print("server started")
	s.listen(1)
	while True:
		client,addr = s.accept()
		print("connection from: "+str(addr))
		threading.Thread(target = example, args=(client, )).start()
		


def example(c):
	guessvalue = random.randint(1,50)
	print("guess is"+str(guessvalue))
	data = c.recv(1024).decode()
	count = 0
	grater = "Your number is grater than guessvalue"
	lesser = "Your number is lesser than guessvalue"
	while int(data) != guessvalue:
		data = int(data)
		if data > guessvalue:
			c.send(grater.encode())
		elif data < guessvalue:
			c.send(lesser.encode())
			break
		count = count+1
		data = c.recv(1024).decode()
	equal = "Correct, Number of guesses are: "+str(count)
	c.send(equal.encode())
	c.close()
if __name__ =="__main__":
	main()		