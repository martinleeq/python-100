"""
问题41
有一个列表[1,2,3,4,5,6,7,8,9,10],使用map()生成一个新的列表,新的列表的元素为原来列表元素的平方
"""

def print_map():
    """
    两个知识点:
    1. map()函数,对传入的可迭代对象的每个元素进行迭代,对其执行传入的操作
    2. labmda表达式,也就是其他语言的匿名函数,显使地使用lambda字符串
    """
    pre_list = [x for x in range(1, 11)]
    new_list = list(map(lambda x: x**2, pre_list))
    print(new_list)

print_map()
