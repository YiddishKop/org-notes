# Networking
# Python3 Advanced #5

# What is Net Code?
# Networking is a huge field, so we will stick to high level concepts that are important for programming.
# Networking is the concept of two programs communicating across a network. Whether it be from client-client, client-server or even client to itself.
# Client – An end device interfacing with a human.
# Sever – A device providing a service for clients.

# What is Net Code?
# Client/Server model
# Most common.
# Clients connect in to the server to get information they require.
# Web browser(client) connects to the Google Website(Server)

# What is Net Code?
# Peer-to-Peer model
# Useful for services that don’t have to be constantly available. (Skype, Game Servers)
# Clients connect to other clients without the use of a central server.
# (Is actually a Client/Server model at it’s core, just client’s are acting as a server and client)

# What is Net Code?
# Terminology:
# Address – An IP address, eg “127.0.0.1”
# Port – A port number, eg 5000
# Port numbers 1 – 1024 are reserved for core protocols, Try to use something above 1024 but below 65535.

# Sockets
# Sockets are the programming abstractions for connections.
# They allow us to communicate in a bidirectional manner.
# Once they are connected or ready to transmit.
# We can use them to send data and receive data.
# They implement the common transport protocols TCP and UDP.

# Socket Methods
# socket(socket_family, socket_type)
# The constructer creates a new socket.
# bind((hostname,port))
# Bind takes a turple of a host address and port
# listen()
# Starts listening for TCP connections
# accept()
# Accepts a connection when found.(returns new socket)

# Socket Methods
# connect((hostname,port))
# Takes a turple of the address and port.
# recv(buffer)
# Tries to grab data from a TCP connection.(Waits)The buffer size determines how many bytes of data to receive at a time.
# send(bytes)
# attempts to send the bytes given to it.
# close()
# Closes a socket/connection and frees the port.

# TCP
# Transmission Control Protocol.
# Reliable Connection based Protocol
# Ordered & Error checked (simple checksum)

# Used by Web Browsers, Email, SSH, FTP, etc
# Capitalize Sentence Program
# Lets create a basic client server program that uses TCP to connect and send text to a server the server then replies with that text capitalized.
# We will build the Server first then the Client.
# tcpServer.py and tcpClient.py

import socket
def Main():
    host = '127.0.0.1'
    port = 5000

    # server->s, client->c
    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c, addr = s.accept()
    print("Connection from: " + str(addr))

    while True:
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        print("From connected user: " + data)
        data = data.upper()
        print("Sending: " + data)
        c.send(data.encode('utf-8'))

    c.close()

if __name__ == "__main__":
    Main()
