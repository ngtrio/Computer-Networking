from socket import *
serverName = 'localhost'
serverPort = 12000
clintSocket = socket(AF_INET, SOCK_STREAM)
clintSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence:')
clintSocket.send(sentence.encode())
modifiedSentence = clintSocket.recv(1024)
print('From server:', modifiedSentence.decode())
clintSocket.close()