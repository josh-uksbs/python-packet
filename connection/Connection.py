from connection.thread.PacketSubServerThread import PacketSubServerThread

class Connection:
    def __init__(self, main, address, pipeline):
        self.__address = str(address)
        self.__pipeline = pipeline
        self.__thread = PacketSubServerThread(main, self)
        self.__thread.start()
        self.__can_receive = False


    def get_address(self):
        return self.__address

    
    def get_pipeline(self):
        return self.__pipeline


    def can_receive(self, boolean):
        self.__can_receive = boolean


    def is_receiving(self):
        return self.__can_receive
