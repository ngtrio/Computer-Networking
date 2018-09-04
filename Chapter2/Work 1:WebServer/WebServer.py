from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 10000
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(2048).decode()
        print(message)
        filename = message.split()[1]   # 请求的路径
        f = open(filename[1:])          # 请求的文件名
        outputdata = f.read()
        header = 'HTTP/1.1 200 OK\nContent-Type: text/html'
        connectionSocket.send(header.encode())
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        header = 'HTTP/1.1 404 Not Found\nContent-Type: text/html'
        connectionSocket.send(header.encode())
        connectionSocket.close()