import socket
import socketbase
import time


class Client(socketbase.SocketBase):
    my_ip = ''

    def __init__(self):
        self.my_ip = self.get_my_ip()
        self.ips_not_mine = self.get_ips_not_mine(self.my_ip)

    def run(self, port: int, result: []):

        result = []
        sock = socket.socket(self.SOCKET_TYPE["family"], self.SOCKET_TYPE["type"])
        sock.settimeout(self.TIMEOUT)

        for server_ip in self.ips_not_mine:
            server_address = (server_ip, port)

            while True:
                try:
                    sock.connect(server_address)
                    data_bytes = sock.recv(self.PAYLOAD_SIZE_BYTES)
                    data_int = 0
                    data_int.from_bytes(data_bytes, self.BYTEORDER)
                    result.append(data_int)

                    # successfully exit loop
                    break

                finally:
                    pass

            sock.close()

        # result returned through "result" reference variable
