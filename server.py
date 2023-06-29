import time, socket, sys   # Import necessary modules

new_socket = socket.socket()   # Create a new socket object
host_name = socket.gethostname()   # Get the hostname of the machine running the program
s_ip = socket.gethostbyname(host_name)   # Get the IP address of the machine

port = 8080   # Set the port number to be used by the server

new_socket.bind((host_name, port))   # Bind the socket to the host name and port number
print("Binding Successful!")   # Print message indicating that the socket has been successfully bound
print("This is your IP: ", s_ip)   # Print the IP address of the server

name = input('Enter name: ')   # Prompt the user to enter their name

new_socket.listen(5)   # Set the server to listen for incoming connections

conn, add = new_socket.accept()   # Accept an incoming connection and assign the connection object and address to variables

print("Received connection from ", add[0])   # Print message indicating that a connection has been received from a client
print('Connection Established. Connected From: ',add[0])   # Print the IP address of the client that connected

client = (conn.recv(1024)).decode()   # Receive the client's name from the connection object and decode it
print(client + ' has connected.')   # Print message indicating which client has connected

conn.send(name.encode())   # Send the user's name to the client

while True:   # Loop to send and receive messages
    message = input('Me : ')   # Prompt the user to enter a message to send
    conn.send(message.encode())   # Send the message to the client
    message = conn.recv(1024)   # Receive a message from the client
    message = message.decode()   # Decode the received message
    print(client, ':', message)   # Print the name of the client and the received message to the console
