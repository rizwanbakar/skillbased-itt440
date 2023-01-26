import socket

def main():
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect(("192.168.214.128", 8888))

    # Obtain the quote from the server
    quote = client_socket.recv(1024).decode()
    print("Quote of the Day obtained from the server:", quote)

    # Close the socket
    client_socket.close()

if name == "main":
    main()
