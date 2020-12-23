"""
问题37
生成一个元组, 其元素为1 ~ 21的平方,并输出
"""

def print_tuple():
    a_tuple = (x ** 2 for x in range(1, 21))
    print(a_tuple)
    for item in a_tuple:
        print(item, end=',')

print_tuple()

