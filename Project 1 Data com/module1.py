#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serrverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.bind(('',serrverPort))
serverSocket.listen(1)

#Fill in end
while True:
 	#Establish the connection
 print('Ready to serve...')
 connectionSocket, addr = serverSocket.accept()	 	#Fill in end
 try:
     message = connectionScoket.recv(4096) #Fill in start 		#Fill in end
 filename = message.split()[1]
 f = open(filename[1:])
 outputdata = f.readlines() #Fill in start 		#Fill in end
 #Send one HTTP header line into socket
 #Fill in start
 connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n")
 connectionSocket.send("\r\n")
 #Fill in end
 #Send the content of the requested file to the client
 for i in range(0, len(outputdata)):
    connectionSocket.send(outputdata[i].encode())
 connectionSocket.send("\r\n".encode())
 connectionSocket.close()
# except IOError:
 #Send response message for file not found
 #Fill in start 

 #Fill in end
 		#Close client socket
 #Fill in start
 		#Fill in end
 serverSocket.close()
 sys.exit()#Terminate the program after sending the corresponding data
