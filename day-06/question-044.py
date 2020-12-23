"""
问题44
使用map()函数生成一个列表,其元素是 1 ~ 20 的平方
"""

def print_map():
    a_list = list(map(lambda x: x**2, range(1, 21)))
    print(a_list)


def square(x):
    return x ** 2;

def print_map_function():
    a_list = list(map(square, range(1, 21)))
    print(a_list)

    
print_map()
print_map_function()
