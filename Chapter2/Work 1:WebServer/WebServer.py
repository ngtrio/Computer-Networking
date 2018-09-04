from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 10086
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(2048).decode()
        filename = message.split()[1]   # 请求的路径
        f = open(filename[1:])          # 请求的文件名
        outputdata = f.read()
        header = 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8'
        connectionSocket.send(header.encode())
        # for i in range(0, len(outputdata)):
        connectionSocket.send(outputdata.encode())
        connectionSocket.close()
    except IOError:
        header = 'HTTP/1.1 404 Not Found\nContent-Type: text/html; charset=utf-8'
        connectionSocket.send(header.encode())
        connectionSocket.close()