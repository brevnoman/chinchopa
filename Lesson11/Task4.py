class CustomException(Exception):

    def __init__(self, msg):
        self.msg = msg


raise CustomException("sis")
