#include <stdio.h>
	#include <stdlib.h>
	#include <string.h>
	#include <sys/socket.h>
	#include <netinet/in.h>
	#include <unistd.h>

	int main() {
		int server_socket, client_socket;
		struct sockaddr_in server, client;
		int c, rand_num;
		socklen_t client_len;

		// Creating socket
		server_socket = socket(AF_INET, SOCK_STREAM, 0);
		if (server_socket == -1) {
			printf("Failed to create socket");
		}
		puts("Socket created successfully");

		// Forming the sockaddr_in structure
		server.sin_family = AF_INET;
		server.sin_addr.s_addr = INADDR_ANY;
		server.sin_port = htons(8888);

		// Bind
		if (bind(server_socket, (struct sockaddr *) &server, sizeof(server)) < 0) {
			perror("Error. Bind failed. ");
			return 1;
		}
		puts("Bind done");

		// Listen
		listen(server_socket, 3);

		// Accept connection
		puts("Waiting for connections...");
		client_len = sizeof(struct sockaddr_in);

		while ((client_socket = accept(server_socket, (struct sockaddr *) &client, &client_len))) {
			puts("Connection has been accepted");

			// Generate a random number from 100 to 999 
			rand_num = rand() % 900 + 100;
			
			// Send random number to client
			send(client_socket, &rand_num, sizeof(int), 0);
			printf("Random number sent to client: %d\n", rand_num);

			// Close the socket
			close(client_socket);
			puts("Connection has been closed");
		}

		if (client_socket < 0) {
			perror("Error. Accept failed");
			return 1;
		}

		return 0;
	}
