import socket


class SocketBase:
    PAYLOAD_SIZE_BYTES = 4
    BYTEORDER = "little"

    SOCKET_TYPE = {"family": socket.AF_INET,
                   "type": socket.SOCK_STREAM}

    TIMEOUT = 300

    HARDCODED_IPS = ['10.0.1.50',
                     '10.0.1.192',
                     '10.0.1.193']
    ips_not_mine = []

    @staticmethod
    def get_my_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except:
            IP = '127.0.0.1'
        finally:
            s.close()

        print("My IP:" + str(IP))

        return IP

    def get_ips_not_mine(self, my_ip):
        ips_not_mine = self.HARDCODED_IPS

        for ip in ips_not_mine:
            if ip == my_ip:
                ips_not_mine.remove(ip)

        print("Other ips:" + str(ips_not_mine))

        return ips_not_mine

    def get_server_count(self):
        return len(self.HARDCODED_IPS)
