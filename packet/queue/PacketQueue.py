from packet.thread.PacketQueueThread import PacketQueueThread

class PacketQueue:
    def __init__(self):
        self.__queue = []
        queue_thread = PacketQueueThread(self)
        queue_thread.start()
        self.__last_packet = None


    def add_to_queue(self, packet):
        self.__queue.append(packet)


    def remove_from_queue(self, packet):
        self.__queue.remove(packet)


    def is_empty(self):
        return len(self.__queue) == 0


    def flush(self):
        packet = self.__queue[0]
        print(f"flushing {packet.to_string()}")

        if self.__last_packet != None:
            if packet.get_unique_id() == self.__last_packet.get_unique_id():
                return
            
        self.__last_packet = packet
        
        packet.send()
        self.__queue.pop(0)


    
