"""
问题36
生成一个列表,其中的值为1~20的平方,并输出除了前5个元素之外的其他元素
"""

def print_list_except_top_5():
    a_list = [x ** 2 for x in range(1, 21)]
    print(a_list[5:])

print_list_except_top_5()
