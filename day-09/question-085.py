"""
问题85
给出一个列表[12,24,35,70,88,120,155],移除第0,4,5个元素,并打印列表
"""

raw_list = [12, 24, 35, 70, 88, 120, 155]
filtered_list = [item for (idx, item)in enumerate(raw_list)
                 if idx not in [0, 4, 5]]
print(filtered_list)