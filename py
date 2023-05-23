import socket

# Server configuration
HOST = 'localhost'  # Replace with your server's IP address or hostname
PORT = 12345  # Replace with the desired port number

# Create a socket and bind it to the specified host and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)
print(f"Listening on {HOST}:{PORT}...")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Connected to client: {client_address}")

# Receive the directory listing data from the client
data = client_socket.recv(4096).decode('utf-8')
print("Received data:")
print(data)

# Close the client socket
client_socket.close()

# Close the server socket
server_socket.close()


@echo off

REM Run the dir command and save the output to a temporary file
dir > "%TEMP%\dir_output.txt"

REM Use PowerShell to send the file content to the Python server
powershell -Command "(gc '%TEMP%\dir_output.txt') -join [Environment]::NewLine | python your_server_script.py"

REM Clean up the temporary file
del "%TEMP%\dir_output.txt"

exit
