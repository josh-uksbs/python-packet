from threading import Thread
from packet.Packet import Packet

class PacketSubServerThread(Thread):
    def __init__(self, main, connection):
        Thread.__init__(self)
        self.__main = main
        self.__connection = connection


    def run(self):
        while True:
            result = self.__connection.get_pipeline().recv(1024).decode("utf-8").split(":")
            packet = Packet(result[0], result[1])
            self.__handle_received_packet(packet)


    def __handle_received_packet(self, packet):
        if packet.get_header() == self.__main.CONNECTION_HEADER:
            self.__connection.can_receive(True)
            self.__main.send_received_connection(self.__connection)
            
        print(f"received {packet.to_string()}")

            
                
