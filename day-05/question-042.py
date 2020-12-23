"""
问题42
有一个列表[1,2,3,4,5,6,7,8,9,10],使用map()生成一个新的列表,并用filter()过滤出其中的偶数元素
"""

def print_map_filter():
    pre_list = [x for x in range(1, 11)]

    new_list = list(filter(lambda x: x % 2 == 0, map(lambda x: x**2, pre_list)))
    print(new_list)

print_map_filter()
