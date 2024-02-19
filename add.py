import pickle
from Server import Server

servers = pickle.load(open("servers.pickle", "rb"))

print("Example to add server")

servername = input("Enter server name: ")
port = int(input("Enter a port number as integer: "))
connection = input("Enter a type ping/plain/ssl: ")
priority = input("Enter priority high/low: ")

new_server = Server(servername, port, connection, priority)
servers.append(new_server)

pickle.dump(servers, open("servers.pickle", "wb"))