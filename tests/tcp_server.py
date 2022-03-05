import socket


class TcpServer:
    def __init__(self, ip='127.0.0.1', port=8888):
        self._ip = ip
        self._port = port

    def get_socket(self):
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.bind((self._ip, self._port))
        return soc

    def run(self):
        print(f"Starting TCP server IP:{self._ip} PORT:{self._port}")
        soc = self.get_socket()
        soc.listen(5)
        while True:
            conn, addr = soc.accept()
            from_client = []
            while True:
                try:
                    data = conn.recv(4096)
                except ConnectionResetError:
                    break
                if not data:
                    break
                from_client.append(data)
                print(f'Data received: {from_client}')
                conn.send(f'Received data {from_client}'.encode('UTF-8'))
            conn.close()


if __name__ == '__main__':
    server = TcpServer()
    server.run()
