import argparse
import client
import server
import threading

parser = argparse.ArgumentParser(description="exercise 3")
parser.add_argument('integer', type=int, help='unique machine number [0-2]')

args = parser.parse_args()

print("My Integer:" + str(args.integer))

the_client = client.Client()
the_server = server.Server()

client_result = []

client_thread = threading.Thread(name="client thread", target=the_client.run, args=(1111, client_result, ))
client_thread.start()
server_thread = threading.Thread(name="server thread", target=the_server.run, args=(args.integer, 1111))
server_thread.start()

client_thread.join()
server_thread.join()

print("Other integers: " + str(client_result))
