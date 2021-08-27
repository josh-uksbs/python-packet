import socket
from os import system
from packet.Packet import Packet
from packet.queue.PacketQueue import PacketQueue
from connection.registry.ConnectionRegistry import ConnectionRegistry
from connection.listener.ConnectionListener import ConnectionListener

class Server:
    def __init__(self):
        system("title Server")
        ADDRESS = "localhost"
        PORT = 25565

        self.CONNECTION_HEADER = "CON"

        self.__connection_registry = ConnectionRegistry(self)
        self.__open_connections(ADDRESS, PORT)
        
        self.__packet_queue = PacketQueue()


    def __open_connections(self, ADDRESS, PORT):
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.bind((ADDRESS, PORT))

        self.__connection_listener = ConnectionListener(self.__connection_registry, connection)
        self.__connection_listener.start()



    def get_connection_registry(self):
        return self.__connection_registry


    def send_received_connection(self, connection): 
        packet = Packet(self.CONNECTION_HEADER, "received connection")
        packet.bind(connection.get_pipeline())
        self.__packet_queue.add_to_queue(packet)


server = Server()
    
