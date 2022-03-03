from invoke import task

from core import run, UDPFlooder


@task(help={'address': "Please pass IP address to attack. i.e. 123.12.12.123"})
def attack(c, address):
    run(address)


@task(help={'address': "Please pass IP address with port to attack. i.e. 123.12.12.123:53"})
def udp_flood(c, address):
    UDPFlooder(address).run()
