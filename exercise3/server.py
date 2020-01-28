import socket
import socketbase


class Server(socketbase.SocketBase):
    my_ip = ''
    number_clients = 0

    def __init__(self):
        self.my_ip = self.get_my_ip()
        self.number_clients = self.get_server_count() - 1

    def run(self, value: int, port: int):
        sock = socket.socket(self.SOCKET_TYPE["family"], self.SOCKET_TYPE["type"])
        sock.settimeout(self.TIMEOUT)

        server_address = (self.my_ip, port)
        sock.bind(server_address)
        sock.listen(1)

        data = value.to_bytes(self.PAYLOAD_SIZE_BYTES, self.BYTEORDER)

        for client_id in range(0, self.number_clients):

            connection, client_address = sock.accept()
            try:
                connection.sendall(data)
            finally:
                pass

            connection.close()

        sock.close()
