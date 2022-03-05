"""
Simple TCP server for tests
"""
import asyncio
import socket


async def handle_client(client):
    loop = asyncio.get_event_loop()
    request = None
    while request != 'quit':
        request = await loop.sock_recv(client, 255)
        print(f'Redeived request {request}')
        response = 'You are the best'
        await loop.sock_sendall(client, response.encode('utf8'))
    client.close()


async def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8889))
    server.listen(8)
    server.setblocking(False)

    loop = asyncio.get_event_loop()

    while True:
        client, _ = await loop.sock_accept(server)
        loop.create_task(handle_client(client))


if __name__ == '__main__':
    print('Starting TCP server')
    asyncio.run(run_server())
