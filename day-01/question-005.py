"""
问题5: 定义一个类,这个类中包含两个方法:
    1. getString, 从控制台获取字符串
    2. printString,以大写形式输出字符串
    类中还需要包含一些测试方法
"""

class StringHelper(object):
    def __init__(self) -> None:
        self.str = ''

    def getString(self):
        self.str = input()
        
    def printString(self):
        print(self.str.upper())


if __name__ == "__main__":
    helper = StringHelper()
    helper.getString()
    helper.printString()
