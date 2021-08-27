from threading import Thread

class PacketQueueThread(Thread):
    def __init__(self, packet_queue):
        Thread.__init__(self)
        self.__packet_queue = packet_queue

    def run(self):
        while True:
            if not self.__packet_queue.is_empty():
                self.__packet_queue.flush()
                
