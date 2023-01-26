from socket import *

serverName = '192.168.214.128' #ip address
serverPort = 9999 #port number assigned
  
# TCP socket 
clientSocket = socket(AF_INET, SOCK_STREAM)    
 
clientSocket.connect((serverName, serverPort)) 

temp = input('Enter the temperature in Celsius: ') 
clientSocket.send(temp.encode()) 
#sending to server 

# converted temperature 
tempModified = clientSocket.recv(1024) 

print('After Converting To Fahrenheit:') 
#printing the converted temperature from celsius to fahrenheit #showing the converted temperature here
print(tempModified.decode('utf8','strict'))  

#close socket 
clientSocket.close()
