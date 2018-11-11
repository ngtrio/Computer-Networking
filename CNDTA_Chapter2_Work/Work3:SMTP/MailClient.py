from socket import *

def receive(clientSocket):
    print(clientSocket.recv(1024).decode())

msg = '\r\n I love computer networks!'
endmsg = '\r\n.\r\n'
mailserver = 'smtp.163.com'
clientSocket = socket(AF_INET, SOCK_STREAM)

# 建立TCP连接
clientSocket.connect((mailserver, 25))
recv = clientSocket.recv(1024)
print(recv.decode())
if recv[:3] != '220':
    print('220 reply not received from server.')

# 登录前必须发送HELO
heloCommand = 'HELO Jing\r\n'
clientSocket.send(heloCommand.encode()) 
recv1 = clientSocket.recv(1024)
print(recv1.decode())
if recv1[:3] != '250':
    print('250 reply not received from server.'.encode())

# 登录
clientSocket.send('AUTH LOGIN\r\n'.encode())
receive(clientSocket)
# 邮箱base64加密
clientSocket.send('dGFuZ2ppbmd5YW5nMDYwOEAxNjMuY29t\r\n'.encode())
receive(clientSocket)
# 密码base64加密
clientSocket.send('password\r\n'.encode())
receive(clientSocket)

# 发送邮件
clientSocket.send('MAIL FROM:<tangjingyang0608@163.com>\r\n'.encode())
receive(clientSocket)
clientSocket.send('RCPT TO:<tangjingyang0608@outlook.com>\r\n'.encode())
receive(clientSocket)

## 发送内容
clientSocket.send('DATA\r\n'.encode())
receive(clientSocket)
clientSocket.send('From:tangjingyang0608@163.com\r\n'.encode())
clientSocket.send('To:tangjingyang0608@outlook.com\r\n'.encode())
clientSocket.send('Subject:SMTP Lab Complete!\r\n'.encode())
clientSocket.send(msg.encode())
clientSocket.send(endmsg.encode())
receive(clientSocket)

# 断开连接
clientSocket.send('QUIT\r\n'.encode())
receive(clientSocket)
