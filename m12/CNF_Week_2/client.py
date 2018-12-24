import socket

def main():
	host = '10.10.8.239'
	port = 7677

	sock = socket.socket()
	sock.connect((host,port))
	print("welcome to ATTENDENCE PORTAL ")
	message = input("Enter your ROLL NUMBER: ")
	while True:
		sock.send(message.encode())
		securityQuestion = sock.recv(1024).decode()
		print(securityQuestion)
		answer = input("Enter your answer:")
		sock.send(answer.encode())
		finalResponse = sock.recv(1024).decode()
		print(finalResponse)
		if(finalResponse == "ATTENDENCE FAILURE" or finalResponse == "ATTENDENCE SUCCESS" or finalResponse == "ROLL-NUMBER NOT FOUND"):
			break
		# print(str(data))
		# num = str(data).split(':')
		# if len(num) == 2:
		# 	break	
	sock.close()
if __name__ == "__main__":
	main()	