from threading import Thread
from packet.Packet import Packet

class PacketSubClientThread(Thread):
    def __init__(self, pipeline):
        Thread.__init__(self)
        self.__pipeline = pipeline


    def run(self):
        while True:
            result = self.__pipeline.recv(1024).decode("utf-8").split(":")
            packet = Packet(result[0], result[1])
            self.__handle_received_packet(packet)


    def __handle_received_packet(self, packet):
        print(f"received {packet.to_string()}\n")
            
                
