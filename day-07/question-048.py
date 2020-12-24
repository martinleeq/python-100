"""
问题48
定义一个名为Rectangle的类,传入长度和宽度,并声明一个计算面积的方法
"""

class Rectangle(object):
    
    def __init__(self, length, width) -> None:
        self.__length = length
        self.__width = width
        
    def area(self):
        return self.__length * self.__width
    
if __name__ == "__main__":
    while True:
        length = int(input('Please input the length: '))
        width = int(input('Please inut the width: '))
        result = Rectangle(length, width).area()
        print(f'The area of {length} * {width} is: {result}')
    