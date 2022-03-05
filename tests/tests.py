import pytest
from core.connection_checkers import TCPChecker, UDPChecker, AddressNotAvailable
from core.validators import AddressWithPortValidator, AddressIsNotValid
from core.utils import Address


@pytest.mark.parametrize("address, error", [
    ('1.1.1.1:443', None),
    ('1.1.1.1', AddressIsNotValid),
])
def test_address_and_port_validation(address, error):
    if not error:
        AddressWithPortValidator(address).validate()
        return
    with pytest.raises(error):
        AddressWithPortValidator(address).validate()


@pytest.mark.parametrize('address, checker, error', [
    ('google.com:443', TCPChecker, None),
    ('google.com:443', UDPChecker, None),
    ('fake-address.as:443', TCPChecker, AddressNotAvailable),
    ('fake-address.as:443', UDPChecker, AddressNotAvailable),
])
def test_check_connection_to_real_address(address, checker, error):
    address = Address(address)
    if not error:
        checker(address.get_address(), address.get_port()).check_connection()
        return
    with pytest.raises(AddressNotAvailable):
        checker(address.get_address(), address.get_port()).check_connection()
