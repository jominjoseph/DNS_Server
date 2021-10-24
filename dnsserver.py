
import sys
import socket
import struct
import random
import codecs

# Read server IP address and port from command-line arguments

serverIP = sys.argv[1]
serverPort = int(sys.argv[2])
print("The server is ready to receive on port:  " + str(serverPort) + "\n")
#dnsmastertext = open("dns-master.txt",'r')

def checkinfile(filename,hostname):
    with open(filename, 'r') as mastertext:
        for (line) in mastertext:
            #print(hostname)
            if ((hostname in line)):
               # print("worked")
                return line
            #else:
              #  print(line+" -"+hostname+"is not equal")
    return "-"

# Create a UDP socket. Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Assign server IP address and port number to socket
serverSocket.bind((serverIP, serverPort))



# loop forever listening for incoming UDP messages
while True:
    # Receive and print the client data from "data" socket
    data, address = serverSocket.recvfrom(1024)
    
    recieved = struct.unpack('!HHIHH100s',data)
    messageid = int(recieved[2])
    questionlength= int(recieved[3])
    client_hostname= codecs.decode(recieved[5])
    client_hostname.strip()
    client_hostname2=""
    letters= "abcdefghijklmnopqrstuvwxyz1234567890."
    for element in client_hostname:
        if (element in letters):
            client_hostname2+=element
    print("\n")
    
#    dns2=checkinfile('dns-master.txt',client_hostname2)
#    print(dns2)
#    print(client_hostname+ "i")
    
    
    if(checkinfile("dns-master.txt",client_hostname2)!="-"):
        #print("hi")
        dns=checkinfile("dns-master.txt",client_hostname2)
        answerlength= len(dns)-1
        packet = struct.pack('!HHIHH100s100s',2,0,messageid,questionlength,answerlength,recieved[5],dns.encode())
        serverSocket.sendto(packet,address)
    elif(checkinfile("dns-master.txt",client_hostname2)=="-"):
        nulls= " "
        packet = struct.pack('!HHIHH100s100s',2,1,messageid,questionlength,0,recieved[5],nulls.encode())
        serverSocket.sendto(packet,address)
  #  print(res)
    
       



    # Echo back to client
 

