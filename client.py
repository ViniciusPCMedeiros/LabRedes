from socket import *

serverName = 'localhost'
serverPort = 35000  # Alterado para 35000

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence: ')

clientSocket.sendto(message.encode(), (serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print('Received from server:', modifiedMessage.decode())

clientSocket.close()
