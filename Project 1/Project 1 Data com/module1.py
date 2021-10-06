# import socket module
from threading import Thread
from socket import *
import sys  # In order to terminate the program

serverAddress = '192.168.0.107'
serverSocket = socket(AF_INET, SOCK_STREAM) # Alternative (better) syntax
serverPort = 6789
serverSocket.bind((serverAddress, serverPort))
serverSocket.listen(5)

# Server should be up and running and listening to the incoming connections
#Fill in end
while True:
 	#Establish the connection
 print('Ready to serve...')
 connectionSocket, addr = serverSocket.accept()	 	#Fill in end

 try:
    message = connectionSocket.recv(1024) #Fill in start #Fill in end
    print ("Message is: ", message)
    filename = message.split()[1]
    f = open(filename[1:])
    outputdata = f.readlines() #Fill in start 		
   #Fill in end
    #Send one HTTP header line into socket
    #Fill in start
    connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n".encode())
    #Fill in end
     #Send the content of the requested file to the client
    for i in range(0, len(outputdata)):
        connectionSocket.send(outputdata[i].encode())
    connectionSocket.send("\r\n".encode())
    connectionSocket.close()
 except IOError:
        # Send response message for file not found
        # Fill in start
        connectionSocket.send("HTTP/ 1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        # Fill in end

        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data


