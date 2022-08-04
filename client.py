import socket


socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect(('127.0.0.1', 9000))
cmd = 'GET http://127.0.0.1/romeo.txt HTTP/1.0\r\n\r\n'.encode()
socket_client.send(cmd)

while True:
    data = socket_client.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

socket_client.close()
