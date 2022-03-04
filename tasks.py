from invoke import task

from core import run, UDPFlooder, UDPChecker, TCPChecker, Address, AddressWithPortValidator


@task(help={'address': "Please pass IP address to attack. i.e. 123.12.12.123"})
def attack(c, address):
    run(address)


@task(help={'address': "Please pass IP address with port to attack. i.e. 123.12.12.123:53"})
def udp_flood(c, address):
    UDPFlooder(address).run()


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
