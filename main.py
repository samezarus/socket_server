import socket


SERVER_HOST = 'localhost'
SERVER_PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((SERVER_HOST, SERVER_PORT))

server.listen()

while True:
    # Слушаем порт
    print(f'Server "{SERVER_HOST}" listen port "{SERVER_PORT}"')
    client_socket, client_address = server.accept()

    print(f'Client {client_address} connected')

    while True:
        # Слушаем сообщение от пользователя
        print(f'Listen message from client: {client_address}')
        client_message = client_socket.recv(1024)

        if client_message:
            print(f'send to client')
            server_message = f'Hello {client_address}\n'.encode()
            client_socket.sendall(server_message)
        else:
            break
