import socket
import threading
import sys
import os
import time
import random
import colorama
from socket import *

SERVER_PORT = 2080
client_IP = gethostbyname(gethostname())
sorce_port=13117

class Client():
    def __init__(self,team_name):
        self.teamName = team_name
        self.receievedData = False
        self.udp_socket = socket(AF_INET, SOCK_DGRAM)

    def listenToBroadcast(self):
        # Creates a thread to start listening for broadcasts.
        thread = threading.Thread(target=self.listen)
        thread.start()

    def listen(self):
        s = socket(AF_INET,SOCK_DGRAM)
        print( "Client started, listening for offer requests...")

        # Binds client to listen on port self.port. (will be 13117)
        try:
            self.udp_socket.bind(('', sorce_port))
        except:
            self.listen()
        # Receives Message
        message = self.udp_socket.recvfrom(1024)[0]

        # Message Teardown.
        # magic_cookie = message[:4]
        # message_type = message[4]
        port_tcp = message[5:]
        self.connectTCPServer(int.from_bytes(port_tcp, byteorder='big', signed=False))


    def connectTCPServer(self, ip_tcp, port_tcp):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect to tcp server
        s.connect((sorce_port, port_tcp))
        # Sending team name
        s.send(bytes(self.teamName, encoding='utf8'))

        # Receive data from Server
        data = str(s.recv(1024), 'utf-8')
        print(data)

        # Setting blocking to false, Data to none and removing key presses representation
        data = None
        s.settimeout(0.0)
        #capture characters without press enter?
        os.system("stty raw -echo")
        while True:
            # if data is recieved it will stop and print, else it will send every key press to the server.
            try:
                data = s.recv(1024)
            except:
                pass
            if data:
                os.system("stty -raw echo")
                data = str(data, 'utf-8')
                #self.receievedData = True
                print(data)
                break
            else:
                c = sys.stdin.read(1)
                s.send(bytes(c, encoding='utf8'))
        s.close()