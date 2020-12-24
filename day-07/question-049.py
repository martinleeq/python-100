"""
问题49
定义一个类Shape及其子类Square.Square类的初始化方法接收一个表示长度的参数.两个类都有计算面积的方法,Shape类的面积默认为0.
"""

class Shape(object):
    
    def area(self):
        return 0
    

class Square(Shape):
    
    def __init__(self, length=0) -> None:
        """
        这里可以不显示调用父类的init方法,默认是会调用的
        """
        super().__init__()
        self.__length = length
        
    def area(self):
        return self.__length ** 2
    
if __name__ == "__main__":
    while True:
        length = int(input('Please input the length: '))
        square = Square(length)
        print('The area of {0} is {1}'.format(length, square.area()))