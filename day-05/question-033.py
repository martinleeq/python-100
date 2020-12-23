"""
问题33
生成一个列表,其中的值为1~20的平方,并输出
"""

def print_list():
    a_list = [x ** 2 for x in range(1, 21)]
    print(a_list)

print_list()
