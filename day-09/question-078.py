"""
问题78
给定一个列表[2, 7, 12, 34, 51],对该列表执行shuffle操作
"""

import random
a_list = [2, 7, 12, 34, 51]
count = 5
while count > 0:
    random.shuffle(a_list)
    print(a_list)
    count -= 1