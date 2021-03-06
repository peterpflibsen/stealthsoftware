import socket
import socketbase
import time


class Client(socketbase.SocketBase):
    my_ip = ''

    def __init__(self):
        self.my_ip = self.get_my_ip()
        self.ips_not_mine = self.get_ips_not_mine(self.my_ip)

    def run(self, port: int, result: []):

        for server_ip in self.ips_not_mine:
            server_address = (server_ip, port)

            while True:
                try:
                    sock = socket.socket(self.SOCKET_TYPE["family"], self.SOCKET_TYPE["type"])
                    sock.settimeout(self.TIMEOUT)

                    sock.connect(server_address)
                    data_bytes = bytes()

                    while len(data_bytes) < self.PAYLOAD_SIZE_BYTES:
                        data_bytes += sock.recv(self.PAYLOAD_SIZE_BYTES)

                    data_int = 0
                    data_int = data_int.from_bytes(data_bytes, byteorder=self.BYTEORDER)
                    result.append(data_int)

                    sock.close()

                    # successfully exit loop
                    break

                except ConnectionError:
                    pass

        # result returned through "result" reference variable
