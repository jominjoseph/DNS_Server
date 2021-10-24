

import sys
import socket
import random
import struct
import binascii

# Get the server hostname, port and data length as command line arguments
serverIP = sys.argv[1]
port = int(sys.argv[2])
hostname = sys.argv[3]


clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clientsocket.settimeout(1)
counter=0
for x in range(0, 3):

    print("\nSending Request to "+ str(serverIP)+", " + str(port))
    if (counter==0):
        messageid= random.randint(0,101)
        print("Message ID: " + str(messageid))
        question = str(port)+ " "+ str(hostname)
        questionlength = len(question)
        print("Question Length: " + str(questionlength)+ " bytes")
        answerlength= 0
        print("Answer Length: "+ str(answerlength)+ "bytes")
        hostname = (str(hostname))
        print("Question:" + hostname+ " A IN\n" )
        
        p= (hostname.encode())

        packet = struct.pack('!HHIHH100s',1,0,messageid,questionlength,answerlength,p)
    
    clientsocket.sendto(packet,(serverIP, port))
    #print("sent")
    try:
        #print("try")
        dataEcho, address = clientsocket.recvfrom(1024)
        recieved = struct.unpack('!HHIHH100s100s',dataEcho)
        print("Receieved response from "+ str(serverIP)+", " + str(port))
        print("Return Code: " + str(recieved[1]))
        print("Message ID: " + str(recieved[2]))
        print("Question Length: " + str(recieved[3])+ " bytes")
        print("Answer Length: "+ str(recieved[4])+ " bytes")
        print("Question:" + str((recieved[5]).decode())+ " A IN")
        if (((recieved[6]).decode)!=" "):
            print("Answer:" + str((recieved[6]).decode()))
        
        
    
        
        break;
       
    except:
        print("Request timed Out")
        counter+=1


#Close the client socket
clientsocket.close()
    
