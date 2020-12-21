"""
问题26
定义一个函数, 该函数接收两个数字, 并返回两个数字之和
"""

def add(a, b):
    """
    最简单的加法实现
    在Python中, 更Python化的实现是Lambda表达式: add = lambda a, b: a + b
    """
    return a + b


add = lambda a, b: int(a) + int(b)

a = input('Please input a:\n')
b = input('Please input b:\n')

print(f'{a} + {b} = {add(a, b)}')
print('{0} + {1} = {2}'.format(a, b, add(a, b)))