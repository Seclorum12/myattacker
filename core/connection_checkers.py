import socket
from abc import ABC, abstractmethod


class AddressNotAvailable(Exception):
    def __init__(self, reason=''):
        self._reason = reason

    def __str__(self):
        return f'Address not available. {self._reason}'


class ConncetionChecker(ABC):
    @abstractmethod
    def check_connection(self):
        ...


class SocketChecker(ConncetionChecker, ABC):
    def __init__(self, address, port, timeout=3):
        self._address = address
        self._port = port
        self._timeout = timeout

    @property
    def timeout(self):
        return self._timeout

    @abstractmethod
    def get_socket(self):
        ...

    def check_connection(self):
        s = self.get_socket()
        try:
            s.connect((self._address, int(self._port)))
            s.sendall(self.msg)
            data = s.recv(1024)
            s.shutdown(socket.SHUT_RDWR)
            print(f'Received resonce: {data.decode()}')
        except TimeoutError:
            raise AddressNotAvailable(f'Timeout {self._timeout} seconds')
        except ConnectionRefusedError:
            raise AddressNotAvailable(f'Connection refused')
        except socket.gaierror as err:
            raise AddressNotAvailable(str(err))
        finally:
            s.close()

    @property
    def msg(self):
        return b'putin Huilo'


class UDPChecker(SocketChecker):
    def get_socket(self) -> socket.socket:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(self.timeout)
        return s


class TCPChecker(SocketChecker):
    def get_socket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(self.timeout)
        return s
