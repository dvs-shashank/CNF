import socket
def main():
    host = "10.10.8.239"
    port = 5050
    s = socket.socket()
    s.connect((host, port))
    message = input("enter the message    ")
    while message != 'q':
        s.send(message.encode())
        data = socket.recv(1024).decode()
        # data.decode()
        print("received from server" + str (data))
        message = input("enter the message      ")
    s.close()

if __name__ == '__main__':
    main()


