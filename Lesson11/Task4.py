class CustomException(Exception):

    def __init__(self, msg):
        self.msg = msg

    @classmethod
    def index_error(cls):
        return cls("Кто вы то, я тут один ...")

    @classmethod
    def type_error(cls):
        return cls('Я уже не челове, я зверь ...')


raise CustomException.index_error()
