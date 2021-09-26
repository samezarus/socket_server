"""
НЕ СДЕЛАНО !!!

Cокет-сервер на генераторах ...
"""

import socket
import selectors


selector = selectors.DefaultSelector()


SERVER_HOST = 'localhost'
SERVER_PORT = 5555


def create_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((SERVER_HOST, SERVER_PORT))
    server.listen()

    selector.register(fileobj=server, events=selectors.EVENT_READ, data=listen_client)


def listen_client(server):
    # Слушаем на наличие новых клиентов
    client, client_address = server.accept()

    selector.register(fileobj=client, events=selectors.EVENT_READ, data=send_to_client)


def send_to_client(client):
    # Слушаем сообщение от клиента
    client_message = client.recv(1024)

    if client_message:
        # Отвечаем клиенту
        server_message = f'Hello client\n'.encode()
        client.sendall(server_message)
    else:
        selector.unregister(client)
        client.close()


def event_loop():
    while True:
        events = selector.select()

        for key, _ in events:
            callback = key.data  # Функция из параметра selector.register(fileobj=..., events=..., data=<функция>)
            callback(key.fileobj)

if __name__ == '__main__' :
    create_server()
    event_loop()

