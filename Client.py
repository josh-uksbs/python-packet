import socket
from os import system
from packet.thread.PacketSubClientThread import PacketSubClientThread
from packet.Packet import Packet
from packet.queue.PacketQueue import PacketQueue

system("title Client")

ADDRESS = "localhost"
PORT = 25565

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((ADDRESS, PORT))

thread = PacketSubClientThread(server)
thread.start()

packet_queue = PacketQueue()

packet = Packet("CON", "successfully connected")
packet.bind(server)
packet_queue.add_to_queue(packet)

