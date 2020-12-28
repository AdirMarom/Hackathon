from hackathon.Client import Client
from hackathon.Server import Server


def main():
    server = Server()
    server.startServer()
    client=Client("adir_team")
    client.listenToBroadcast()



if __name__ == '__main__':
    main()