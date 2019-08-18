import socket
import socketserver
import time
import threading


PORT = 9997

scales_catalogue = set()

def create_broadcast_socket():
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    udp_sock.settimeout(2)
    return udp_sock

def ask_addresses():
    with create_broadcast_socket() as sock:
        sock.sendto('show yourself'.encode('utf-8'), ('255.255.255.255', PORT))




class NetworkController(socketserver.StreamRequestHandler):
    def handle(self):
        request_type = self.rfile.readline()
        #print("{} wrote: {}".format(self.client_address[0], request_type))
        if request_type.decode('UTF-8') == 'I am here\n':
            scales_catalogue.add(self.client_address[0])


class ThreadedServer(object):

    def __init__(self, host, port):
        socketserver.TCPServer.allow_reuse_address = True
        self.server = socketserver.TCPServer((host, port), NetworkController)
        self.server_thread = threading.Thread(target=self.server.serve_forever)



    def start(self):
        self.server_thread.start()


    def stop(self):
        self.server.shutdown()
        self.server.server_close()

def hunt():
    server = ThreadedServer('', PORT)
    server.start()
    ask_addresses()
    time.sleep(1)
    server.stop()
    return scales_catalogue