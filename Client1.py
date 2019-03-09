#TCP socket, client, example 2
#this client connects to the server given with the IP and Port# below and sends a message to server
from socket import *
serverName="192.168.1.190"
serverPort=12000

clientSocket=socket(AF_INET,SOCK_STREAM)

clientSocket.connect((serverName,serverPort))



print('Enter your username for quiz')
msg=input('')
if(msg != ''):
    clientSocket.send(msg.encode())
    
counter = 0
while True:
    if ( counter == 6):
        result=clientSocket.recv(1024)
        print(result.decode("utf-8"))
        clientSocket.close()
        exit(0)
    modifiedMessage=clientSocket.recv(1024)
    print ('This is your question:', modifiedMessage.decode("utf-8"))
    message=input('What is your answer:')

    clientSocket.send(message.encode())
    counter += 1
    if message=="exit":
        clientSocket.close()
        exit(0)
    else :
        print ("message is sent")


