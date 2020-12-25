"""
问题83
给出一个列表[12,24,35,70,88,120,155], 移除第2-4个元素,并打印列表
"""

raw_list = [12, 24, 35, 70, 88, 120, 155]

filterd_list = [item for (idx, item) in enumerate(raw_list)
                if idx < 2 or idx > 4]
print(filterd_list)