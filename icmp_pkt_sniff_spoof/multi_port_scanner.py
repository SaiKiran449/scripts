#!/usr/bin/env python3
import socket
import sys


def scan_ports(ip_address, initial_port, end_port):
    """
    This function will iterate through the port range and detect the open ports
    :param ip_address: The IP Address on which the port scanning has to be done
    :param initial_port: The start range of the port
    :param end_port: The end range of the port
    :return: List of open ports
    """
    open_ports = []

    for port in range(initial_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)  # Set a timeout for the connection attempt
                s.connect((ip_address, port))
                open_ports.append(port)
        except (socket.timeout, ConnectionRefusedError):
            pass

    return open_ports


def validate_input(input_length):
    if input_length != 4:
        sys.exit(1)


validate_input(len(sys.argv))

ip_address = sys.argv[1]
initial_port = int(sys.argv[2])
end_port = int(sys.argv[3])

open_ports = scan_ports(ip_address=ip_address, initial_port=initial_port, end_port=end_port)

if open_ports:
    for port in open_ports:
        print(f"Port {port} open")
else:
    print(f"No open ports found on {ip_address}")

