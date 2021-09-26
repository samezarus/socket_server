"""
Сокет-сервер на очередях
"""

import socket
from select import select


SERVER_HOST = 'localhost'
SERVER_PORT = 5555

for_monitoring = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((SERVER_HOST, SERVER_PORT))
server.listen()


def listen_client(server_socket):
    # Слушаем на наличие новых клиентов
    client, client_address = server.accept()
    for_monitoring.append(client)


def send_to_client(client):
    # Слушаем сообщение от клиента
    client_message = client.recv(1024)

    if client_message:
        # Отвечаем клиенту
        server_message = f'Hello client\n'.encode()
        client.sendall(server_message)
    else:
        client.close()


def event_loop():
    while True:
        ready_to_read, _, _ = select(for_monitoring, [], [])   # read, write, error

        for sock in ready_to_read:
            if sock is server:
                listen_client(sock)
            else:
                send_to_client(sock)


if __name__ == '__main__' :
    for_monitoring.append(server)
    event_loop()

