from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 10086))
serverSocket.listen(2)

while True:
    print('ready to serve...')
    connectionSocket, address = serverSocket.accept()
    message = connectionSocket.recv(4096).decode()
    print('request:\n' + message)
    filename = message.split()[1].partition('/')[2]
    print('filename:' + filename)
    try:
        f = open(filename)
        outputdata = f.read()
        connectionSocket.sendall(outputdata.encode())
    except IOError:
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((filename.partition('/')[0], 80))
        request = message.replace(message.split()[1], '/' + filename.partition('/')[2])
        print(request)
        request = message.replace('127.0.0.1:10086', filename.partition('/')[0])
        print(request)
        clientSocket.sendall(request.encode())
        recv = clientSocket.recv(4096)
        file = open('./' + filename, 'w')
        file.write(recv.decode())
        connectionSocket.sendall(recv)
        clientSocket.close()
        file.close();
    connectionSocket.close()



