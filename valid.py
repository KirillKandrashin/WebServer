import socket
from typing import Any



def port_validation(value: Any, check_open: bool = False) -> bool:
    try:
        value = int(value)

        if 1 <= value <= 65535:
            if check_open:
                return check_port_open(value)
            print(f"Correct port value : {value}")
            return True

        print(f"Incorrect port value : {value}")
        return False

    except ValueError:
        print(f"Value {value} is NOT int!")
        return False

def check_port_open(port: int) -> bool:
    try:
        sock = socket.socket()
        sock.bind(("", port))
        sock.close()
        print(f"Port {port} is free")
        return True
    except OSError:
        print(f"Port {port} is busy")
        return False


def ip_validation(address: str) -> bool:
    error_message = f"Incorrect ip-address {address}"
    ok_message = f"Correct ip-address {address}"
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:
        try:
            socket.inet_aton(address)
        except socket.error:
            print(error_message)
            return False
        return address.count(".") == 3
    except socket.error:
        print(error_message)
        return False

    print(ok_message)
    return True
