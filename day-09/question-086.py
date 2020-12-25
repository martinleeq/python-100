"""
问题86
给出一个列表[12,24,35,24,88,120,155],移除元素24,打印剩下的列表
"""

raw_list = [12, 24, 35, 24, 88, 120, 155]
filter_list = [item for item in raw_list if item != 24]
print(filter_list)