from socket import *

serverPort = 35000  # Alterado para 35000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print(f'The server is ready to receive on port {serverPort}')

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    decodedMessage = message.decode()
    
    # Printa a mensagem recebida e o endereço do cliente
    print(f"Received from {clientAddress}: {decodedMessage}")
    
    modifiedMessage = decodedMessage.upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
