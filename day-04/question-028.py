"""
问题28
定义一个方法, 计算两个字符串形式的数字之和并输出
"""

def add(a, b):
    """
    考察点:
    1. 字符串转换成数字型
    2. lambda表达式
    """
    return int(a) + int(b)

add_ops = lambda a, b: int(a) + int(b)

print(add('2', '8'))
print(add_ops('2', '8'))