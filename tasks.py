from invoke import task

from core import run


@task(help={'address': "Please pass IP address to attack. i.e. 123.12.12.123"})
def attack(c, address):
    run(address)
