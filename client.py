import time, socket, sys   # Import necessary modules

socket_server = socket.socket()   # Create a new socket object

server_host = socket.gethostname()   # Get the hostname of the machine running the program
ip = socket.gethostbyname(server_host)   # Get the IP address of the machine

sport = 8080   # Set the port number to be used by the client

print('This is your IP address: ',ip)   # Print the IP address of the client

server_host = input('Enter friend\'s IP address:')   # Prompt the user to enter the IP address of the server
name = input('Enter Friend\'s name: ')   # Prompt the user to enter the name of the server

socket_server.connect((server_host, sport))   # Connect to the server using its IP address and port number

socket_server.send(name.encode())   # Send the user's name to the server

server_name = socket_server.recv(1024)   # Receive the server's name from the connection object and decode it
server_name = server_name.decode()

print(server_name,' has joined...')   # Print message indicating that the server has joined

while True:   # Loop to send and receive messages
    message = (socket_server.recv(1024)).decode()   # Receive a message from the server and decode it
    print(server_name, ":", message)   # Print the name of the server and the received message to the console
    message = input("Me : ")   # Prompt the user to enter a message to send
    socket_server.send(message.encode())   # Send the message to the server
