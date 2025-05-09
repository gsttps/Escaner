#!/usr/bin/env python3

print(r"""

╔═══╗───────────────────╔╗──────────────╔╗
║╔══╝───────────────────║║─────────────╔╝╚╗
║╚══╦══╦══╦══╦═╗╔══╦═╗╔═╝╠══╗╔══╦╗╔╦══╦╩╗╔╬══╦══╗
║╔══╣══╣╔═╣╔╗║╔╗╣║═╣╔╝║╔╗║║═╣║╔╗║║║║║═╣╔╣║║╔╗║══╣
║╚══╬══║╚═╣╔╗║║║║║═╣║─║╚╝║║═╣║╚╝║╚╝║║═╣║║╚╣╚╝╠══║
╚═══╩══╩══╩╝╚╩╝╚╩══╩╝─╚══╩══╝║╔═╩══╩══╩╝╚═╩══╩══╝
─────────────────────────────║║
─────────────────────────────╚╝
""")	


import socket

def scan_ports(ip, start_port, end_port):
    puertos_abiertos = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) 
        result = sock.connect_ex((ip, port))
        if result == 0:
            puertos_abiertos.append(port)
            print(f"El puerto {port} está abierto")
        sock.close()
    return puertos_abiertos

if __name__ == "__main__":
    scan_ports("127.0.0.1", 1, 1024)