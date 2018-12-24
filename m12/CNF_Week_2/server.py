import socket
import threading 
import random
import csv
def main():
	host = '10.10.8.239'
	port = 7677

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host,port))
	print("server started")
	s.listen(1)
	while True:
		client,addr = s.accept()
		print("connection from: "+str(addr))
		threading.Thread(target = example, args=(client, )).start()
		


def example(c):
	rows = []
	flag = 0
	with open('data.csv', 'r') as csvFile:
		reader = csv.reader(csvFile)
		for each in reader:
			rows.append(each)
	data = c.recv(1024).decode()
	for i in range(len(rows)):
		for j in range(0,3):
			k = j
			if(rows[i][j] == str(data)):
				k = j
				stri = rows[i][k + 1]
				print(stri)
				c.send(stri.encode())
				answer = c.recv(1024).decode()
				if(answer == rows[i][k +2]):
					print('Your answer is',answer)
					print('Actual answer is',rows[i][k +2])
					abc = "ATTENDENCE SUCCESS"
					flag = 1
					c.send(abc.encode())
					break
				else:
					abc = "ATTENDENCE FAILURE"
					c.send(abc.encode())
					break
	if (flag == 0):
		ss = "ROLL-NUMBER NOT FOUND"
		c.send(ss.encode())


	# count = 0
	# grater = "Your number is grater than guessvalue"
	# lesser = "Your number is lesser than guessvalue"
	# while int(data) != guessvalue:
	# 	data = int(data)
	# 	if data > guessvalue:
	# 		c.send(grater.encode())
	# 	elif data < guessvalue:
	# 		c.send(lesser.encode())
	# 		break
	# 	count = count+1
	# 	data = c.recv(1024).decode()
	# equal = "Correct, Number of guesses are: "+str(count)
	# c.send(equal.encode())
	c.close()
if __name__ =="__main__":
	main()		