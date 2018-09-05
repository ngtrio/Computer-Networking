from socket import *
import time

serverPort = 12000
serverName = 'localhost'
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = 'hello'
clientSocket.settimeout(1)  # 设置等待时间
for i in range(10):
    try:
        begin = time.clock()
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        response = clientSocket.recv(1024)
        print(response.decode(), '{}ms'.format(time.clock() - begin))
    except timeout:
        print('loss') 