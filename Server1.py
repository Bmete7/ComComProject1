#TCP socket, threaded server, example 2
#this server receives a message from client and print it on screen, then wait for another connection requests as well as listen for connected clients

from socket import *
import threading

class ThreadedServer():

    def listenToClient(self, client, addr):

            counter=0
            self.usernameTaken=False
            answers=[]
            self.userName= client.recv(1024)
            print(self.userName.decode("utf-8")) 
            while True:
                
                if counter==6:
                    self.assessment(addr,answers)
                    print (addr , " is closed")
                    client.close()
                    exit(0)

                client.send(self.questions[counter].encode())
                message= client.recv(1024)
                if message=="exit":
                    print (addr , " is closed")
                    client.close()
                    exit(0)

                else:
                    counter +=1
            
                    answers.append(message.decode("utf-8"))
    		          

    def assessment(self,addr,answers):

        point = 0
        print(answers)
        if(answers[0]=="a"):
            point +=1
        if(answers[1]=="a"):
            point +=1
        if(answers[2]=="a"):
            point +=1
        if(answers[3]=="c"):
            point +=1
        if(answers[4]=="d"):
            point +=1
        if(answers[5]=="a"):
            point +=1   
        print("Your Socket Information:: ",str(addr[0]) + ":" +str(addr[1]),"Your Username:", self.userName.decode("utf-8"), "Your grade:"  + str(point) + "/6")        
        if(point<2):
            print("poor performance. you should study hard")
        elif(point<4):
            print("average performance. you are mediocre")
        elif(point<=5):
            print("almost perfect. just study the details")
        else:
            print("great performance. you are excellent")

           

    def __init__(self,serverPort):

        self.questions=['''which version of http is stateless? 
        a)http1.0
        b)http1.1
        c)both
        d)none''',
        '''when we prefer ftp instead of http in file transfer?
        a)for big amount of data transfer
        b)sending email to friend
        c)download image from website
        d)instant messaging''',
        '''what is the main difference between end-to-end communication and node-to-node communication?
        a)physical connection is necessary for node-to-node ralation.
        b)being in same localhost
        c)having same default dns server
        d)having same gateway''',
        '''which one of below is not application layer protocol?
        a)http
        b)smtp
        c)tcp
        d)ftp''',
        '''select the one which is not application layer protocol architecture?
        a)hybrit
        b)P2P
        c)Client-Server
        d)switching''',
        '''Select the one which dns maps with the domain name
        a)IP
        b)MAC
        c)socket number
        d)process ID'''
        ]

        self.answers=[]
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
	
