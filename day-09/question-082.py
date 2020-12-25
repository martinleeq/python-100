"""
问题82
给出一个列表[12,24,35,70,88,120,155],移除其中第0,2,4,6个元素,并打印列表
"""

raw_list = [12, 24, 35, 70, 88, 120, 155]

filtered_list = [raw_list[i] for i in range(len(raw_list)) if i % 2 != 0]
print(filtered_list)