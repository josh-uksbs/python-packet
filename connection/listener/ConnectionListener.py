from threading import Thread

class ConnectionListener(Thread):
    def __init__(self, connection_registry, connection):
        Thread.__init__(self)
        self.__connection_registry = connection_registry
        self.__connection = connection


    def run(self):
        while True:
            self.__connection.listen()
            
            pipeline, address = self.__connection.accept()
            print(f"accepted connection {address}")
            self.__connection_registry.add_connection(address, pipeline)
