from connection.Connection import Connection

class ConnectionRegistry:
    def __init__(self, main):
        self.__connections = []
        self.__main = main


    def add_connection(self, address, pipeline):
        self.__connections.append(Connection(self.__main, address, pipeline))


    def remove_connection(self, address):
        connection = self.get_connection(address)

        if connection != None:
            self.__connections.remove(connection)
            connection = None


    def get_connections(self):
        return self.__connections


    def get_connection(self, address):
        for connection in self.__connections:
            if connection.get_address == address:
                return connection

        return None
