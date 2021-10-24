# DNS_Server
DNS server and client

The client will perform the following functions: 
1. Read in 3 arguments from the command line: 
a. IP address of server (127.0.0.1) 
b. Port of server (e.g. 9999) 
c. Hostname (e.g. host1.student.test) 
2. Send a request with the specified hostname to the server using the message format specified  
3. Wait for a response using a 1 second timeout period. 
a. If  a response arrives within the timeout period, print out the server response as shown in 
this document 
b. If not, re-send the message (same sequence number) for a maximum of 3 attempts before 
printing an applicable message and exiting 
 
The server will perform the following functions: 
1. Read in 2 arguments from the command line: 
a. IP address of server (127.0.0.1) 
b. Port of server (e.g. 9999) 
2. Read in the master file named “dns-master.txt” (See “dns-master.txt” for format and example. OK to 
have this filename hard-coded.)  
3. Store the resource records (type A) in data structures in main memory suitable for searching  
4. Respond to requests from the DNS client for hostnames in the domain using the message format 
specified   
5. Return an error if the name queried does not exist in the domain. 
6. The program should still work if the master file is modified to include different hostnames, or IP 
addresses 
