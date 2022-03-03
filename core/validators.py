from abc import ABC, abstractmethod


class AddressIsNotValid(ValueError):
    def __init__(self, reason=''):
        self._reason = reason

    def __str__(self):
        return f'Address is not valid. {self._reason}'


class Validator(ABC):
    @abstractmethod
    def validate(self):
        ...


class IpWithPortValidator(Validator):
    ...


class DomainWithPortValidator(Validator):
    ...


class AddressWithPortValidator(Validator):
    def __init__(self, address: str):
        self._address = address

    def validate(self):
        if len(self._address.split(':')) < 2:
            raise AddressIsNotValid('Required <address>:<port>')
