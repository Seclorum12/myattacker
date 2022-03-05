from time import sleep

from invoke import task
from threading import Thread
from core import UDPFlooder, UDPChecker, TCPChecker, Address, AddressWithPortValidator


@task(help={'address': "Please pass IP address with port to attack. i.e. 123.12.12.123:53"})
def udp_flood(c, address):
    flooder = UDPFlooder(address)
    flooder_thread = Thread(target=flooder.run, daemon=True)
    flooder_thread.start()
    while True:
        sleep(5)
        flooder.print_rate()


@task(help={'address': "Please pass IP address or domain address with port. i.e. 123.12.12.123:53 or domain.com:443"})
def check_udp_connection(c, address):
    AddressWithPortValidator(address).validate()
    address = Address(address)
    UDPChecker(
        address.get_address(),
        address.get_port()
    ).check_connection()
    print('Address is richable')


@task(help={'address': "Please pass IP address or domain address with port. i.e. 123.12.12.123:53 or domain.com:443"})
def check_tcp_connection(c, address):
    AddressWithPortValidator(address).validate()
    address = Address(address)
    TCPChecker(
        address.get_address(),
        address.get_port()
    ).check_connection()
    print('Address is richable')
