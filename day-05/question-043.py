"""
问题43
使用filter()生成一个列表,列表中的元素是1-20之间的偶数
"""

def print_filter():
    a_list = [x for x in range(1, 21)]
    b_list = list(filter(lambda x:x%2==0, a_list))
    print(b_list)

print_filter()
