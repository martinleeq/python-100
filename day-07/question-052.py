"""
问题52
自定义一个异常类,接收一个message参数
"""


class CustomError(Exception):

    def __init__(self, message) -> None:
        super().__init__(message)
        self.__message = message

    def __str__(self) -> str:
        return self.__message


try:
    raise CustomError('This is a custom error raised by myself')
except CustomError as err:
    print(err)
    print('Haha, catch you!')
finally:
    print('Over')
