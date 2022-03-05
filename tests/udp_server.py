import socket


class UdpServer:
    def __init__(self, ip='127.0.0.1', port=8888):
        self._ip = ip
        self._port = port

    def get_socket(self):
        soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        soc.bind((self._ip, self._port))
        return soc

    def run(self):
        print(f"Starting UDP server IP:{self._ip} PORT:{self._port}")
        soc = self.get_socket()
        while True:
            data, addr = soc.recvfrom(1024)
            print("Request data: " + data.decode())
            soc.sendto(b'putin Huilo', addr) if data else None


if __name__ == '__main__':
    server = UdpServer()
    server.run()
