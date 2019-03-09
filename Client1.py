#TCP socket, threaded server, example 2
#this server receives a message from client and print it on screen, then wait for another connection requests as well as listen for connected clients

from socket import *
import threading

class ThreadedServer():


    def listenToClient(self, client, addr):
        
            while True:

                    
                    
            
                #question="which version of http is stateless? \n a)http1.0 \n b)http1.1 \n c)both \n d)none"
                x ="a"
                client.send(self.questions[1].encode())
                message= client.recv(1024)
                if message=="exit":
                    print (addr , " is closed")
                    client.close()
                    exit(0)
                print("Gelen Cevap:" , message.decode("utf-8"))
		

    def __init__(self,serverPort):

        self.questions=["aa","bb","cc","dd","ee"]
        try:
            self.serverSocket=socket(AF_INET,SOCK_STREAM)

        except:
    
            print ("Socket cannot be created!!!")
            exit(1)
            
        print ("Socket is created...")

        try:
           self.serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        except:
    
            print ("Socket cannot be used!!!")
            exit(1)

        print ("Socket is being used...")

        try:
            self.serverSocket.bind(('',serverPort))
        except:
        
            print ("Binding cannot de done!!!")
            exit(1)

        print ("Binding is done...")

        try:
            self.serverSocket.listen(45)
        except:
    
            print ("Server cannot listen!!!")
            exit(1)

        print ("The server is ready to receive")


        while True:

            connectionSocket,addr=self.serverSocket.accept()
            
            threading.Thread(target = self.listenToClient,args = (connectionSocket,addr)).start()
            

if __name__=="__main__":
    serverPort=12000
    ThreadedServer(serverPort)
	
