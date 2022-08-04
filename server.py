import socket


def create_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(('localhost', 9000))
        server_socket.listen(5)
        while True:
            client_socket, address = server_socket.accept()

            read = client_socket.recv(5000).decode()
            pieces = read.split('\n')
            if len(pieces) > 0:
                print(pieces[0])

            data = 'HTTP/1.1 200 OK\r\n'
            data += 'Content-Type: text/html; charset=utf-8\r\n'
            data += '\r\n'
            data += '<html><body>Hello World </body></html>\r\n\r\n'
            client_socket.sendall(data.encode())
            client_socket.shutdown(socket.SHUT_WR)

    except KeyboardInterrupt:
        print()
        print('Shutting down server...')
    except Exception as exception:
        print('Error: ')
        print(exception)

    server_socket.close()


print('Access http://localhost:9000')
create_server()
