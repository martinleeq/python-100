"""
问题47
定义一个圆形Circle类,可以传入半径Radius,并在类中声明一个方法用于计算该圆形的面积
"""

from math import pi

class Circle(object):

    def __init__(self, radius) -> None:
        self.__radius = radius

    def radius(self):
        return self.__radius

    def area(self):
        return pi * self.__radius * self.__radius


circle = Circle(10)
print('Area of circle with radius: {0} is {1}'.format(circle.radius(), circle.area()))
