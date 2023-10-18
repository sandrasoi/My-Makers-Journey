<h1>Week7</h1>

<h2>Goals:</h2>

- Explain how code goes from running on your computer to running on a publicly accessible server.
- Explain how continuous integration and deployment (CI-CD) is used in software teams.
- Deploy a database-backed web application to the cloud using CI-CD.

<h3>Monday 16th October</h3>

This module is structured slightly differently to the previous modules. I am learning about cloud deployment and learning about various concepts that explain how the Internet works and how data is transferred from one end to another. As I am researching these concepts I am realising how impressive technology is. I have been using different mediums to learn such as reading, watching YouTube videos and using ChatGPT. ChatGPT has been particularly useful as I am able to test my understanding by requesting questions and answers for each topic as well as requesting concepts such as Internet Protocal Stack to be presented as a story to help me visualise how data is transported. 

Ping is a command line tool that sends packets to a given location and sends back packets if a connection is working. Traceroute is a tool that traces the route a signal takes from the host to a server. This can be useful as it can identify if there are any issues in the network and where it is located. The way data is transmitted is not in one go by establish one connection between the host and server. This would require too many connections and wouldn't work. There are two solutions to this: breaking down information into packets, and having routers that can pass data to the next router. For example 10 connections going to one router, can then be sent using one connection to the next router. To help me visualise this, I established a connection with a remote server using telnet. Telnet creates a connection allowing me to interact with a server as if I was using it physically. I then used termshark to actually see what packs are being sent to the server.

The way data is sent through the Internet can be explained using the Internet Protocol stack. At the top layer is the application and a request can be sent using a http request. The domain name system (DNS) translates domain names into IP addresses. Then this data is broken down into segments at the transport layer. Transmission Control Protocol works at the transport layer to ensure all the packets are transmitted and if they are not, the lost packet gets resent. It is also involved in establishing a connection with the server before data is transmitted. It does this using the three way handshake, it sends SYN to check the server is receiving it, then if the server responds with SYN/ACK, TCP sends ACK back and then begins data transmission. At the next layer of the Internet Stack, we have the network layer which uses the IP addresses to determine the best route to take to the destination. It also encpaulsates the segments into packets so that each packet includes a segment header of where the packet is going. Then the link layer encapsulates the network layer into frames so that it is ready to be transmitted across the physical medium. This is the physical and finaly layer of the Internet Protocol stack.  

<h3>Tuesday 17th October</h3>

Today I tested my understanding and reviewed the concepts I covered yesterday such as ping, traceroute, telnet, termshark, Internet Protocol stack and IP addresses. 

I delved deeper into understanding how domain name system works to translate domain names into IP addresses. I used nslookup tool to check the IP addresses of specific domains. There are two domain name system records, A records and CNAME records. A records provide IP addressed directly, CNAME records refer to another domain and then use that domains IP address. 

I learned about what has been told to maintain security of data across the Internet. When the Internet was first created, any information could have been intercepted. This problem was solved in 1979 using a Public-Key Cryptography. Public and private keys would be created. The public key would be provided to encode information and the private key would not be sent anywhere but used to decode the information. 

I learned about the rise of cloud computing and why it's preferred over using physical servers. Cloud allows scalability and removes the need to maintain servers. 
