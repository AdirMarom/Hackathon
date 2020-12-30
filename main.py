from Client import startClient
from Server import startServer
import curses 


def main(stdscr):
    server=Server()
    server.startServer()
    client=Client("dor's team")
    client.listenToBroadcast()
    


if _name_ == '_main_':
    main()