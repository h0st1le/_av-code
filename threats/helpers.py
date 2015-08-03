import socket
import time
import string
import random
from datetime import datetime


#http://stackoverflow.com/questions/319279/how-to-validate-ip-address-in-python
def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False
    return True


def is_valid_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:  # not a valid address
        return False
    return True


def get_epoch_timestamp():
    pattern = '%Y-%m-%d %H:%M:%S'
    current_time = datetime.utcnow().strftime(pattern)
    epoch = int(time.mktime(time.strptime(current_time, pattern)))
    return epoch


def create_random_string():
    return ''.join(random.SystemRandom().choice(
        string.ascii_uppercase + string.digits) for _ in range(12))
