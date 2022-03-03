class Address:
    def __init__(self, address):
        self._address = address

    @property
    def raw(self):
        return self._address

    def split_by_port(self):
        return self._address.split(':')

    def get_address(self):
        return self.split_by_port()[0]

    def get_port(self):
        return self.split_by_port()[1]
