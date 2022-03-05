import socket
from abc import ABC, abstractmethod
from .utils import Address


class Attacker(ABC):
    def __init__(self, address):
        self._address = Address(address)
        self._requsets_sent = 0
        self._time_started = None

    @property
    def time_started(self):
        return self._time_started

    @time_started.setter
    def time_started(self, value):
        self._time_started = value

    @property
    def address(self):
        return self._address

    @abstractmethod
    def run(self):
        ...


class SocketAttacker(Attacker, ABC):
    @abstractmethod
    def get_socket(self) -> socket.socket:
        ...
