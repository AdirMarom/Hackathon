from Client import Client
from Server import Server


def main():
    server=Server()
    server.start()
    client=Client("adir_ben_team")
    client.start_client()
    

if _name_ == '_main_':
    main()