import random
import socket
import threading

# Quotes list
quotes = [
    "You must be the change you wish to see in the world - Mahatma Gandhi.",
    "Get busy living or get busy dying. - Stephen King",
    "If you’re going through hell, keep going. - Winston Churchill",
    "Life is like a box of chocolates. You never know what you’re going to get. - Forrest Gump",
    "That’s one small step for a man, one giant leap for mankind. - Neil Armstrong",
]

def handle_client(client_socket):
    
    # Send a quote to client randomly
    client_socket.send(random.choice(quotes).encode())
    client_socket.close()

def main():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind
    server_socket.bind(("192.168.214.128", 8888))

    # Listen
    server_socket.listen()

    while True:
        # Accept a new client connection
        client_socket, client_address = server_socket.accept()

        # Handle the client in a new thread
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if name == "main":
main()
