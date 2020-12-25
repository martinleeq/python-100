"""
问题81
给出一个列表[12,24,35,70,88,120,155],去掉能同时整除5和7的元素,并打印列表
"""

raw_list = [12, 24, 35, 70, 88, 120, 155]
# 列表推导式
filtered_list = [i for i in raw_list if i % 35 != 0]
print(filtered_list)

print('==============')

new_filtered_list = list(filter(lambda x: x % 35 != 0, raw_list))
print(new_filtered_list)