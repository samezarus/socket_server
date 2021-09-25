"""
Синхронный сокет-сервер
"""

import socket


SERVER_HOST = 'localhost'
SERVER_PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((SERVER_HOST, SERVER_PORT))

server.listen()


def wait_client(server_socket):
    while True:
        # Слушаем порт
        #print(f'Server "{SERVER_HOST}" listen port "{SERVER_PORT}"')
        client, client_address = server.accept()
        #print(f'Client {client_address} connected')

        send_to_client(client=client, address=client_address)


def send_to_client(client, address):
    while True:
        # Слушаем сообщение от пользователя
        print(f'Listen message from client: {address}')
        client_message = client.recv(1024)

        if client_message:
            print(f'send to client')
            server_message = f'Hello {address}\n'.encode()
            client.sendall(server_message)
        else:
            break

    client.close()

if __name__ == '__main__' :
    wait_client(server)