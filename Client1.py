#TCP socket, client, example 2
#this client connects to the server given with the IP and Port# below and sends a message to server
from socket import *
serverName="192.168.1.190"
serverPort=12000

clientSocket=socket(AF_INET,SOCK_STREAM)

clientSocket.connect((serverName,serverPort))
userNameGiven = False

while True:
    if  (userNameGiven == False):
        modifiedMessage=clientSocket.recv(1024)
        print(modifiedMessage.decode("utf-8"))
        msg=input('')
        if(msg != ''):
            userNameGiven = True
            clientSocket.send(msg.encode())
    else:
        modifiedMessage=clientSocket.recv(1024)
        print ('This is your question:', modifiedMessage.decode("utf-8"))
        message=input('What is your answer:')

        clientSocket.send(message.encode())
        if message=="exit":
            clientSocket.close()
            exit(0)
        else :
            print ("message is sent")

