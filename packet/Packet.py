import uuid

class Packet:
    def __init__(self, header, content):
        self.__unique_id = uuid.uuid4()
        self.__value = f"{header}:{content}"


    def get_unique_id(self):
        return self.__unique_id


    def get_value(self):
        return self.__value


    def get_header(self):
        return self.__value.split(":")[0]


    def get_content(self):
        return self.__value.split(":")[1]


    def bind(self, pipeline):
        self.__pipeline = pipeline
        return self


    def send(self):
        self.__pipeline.send(self.__value.encode("utf-8"))


    def to_string(self):
        return "Packet{unique_id=" + str(self.__unique_id) + ", value=" + str(self.__value) + "}"

