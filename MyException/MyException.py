class MyException(Exception):
    def __int__(self,*args):
        self.args=args
class FileErrorException(MyException):
    def __int__(self,message):
        self.message=message