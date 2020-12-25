"""
问题80
将列表[5,6,77,45,22,12,24]中的偶数去掉,然后打印该列表
"""

raw_list = [5, 6, 77, 45, 22, 12, 24]
# 列表推导式
filtered_list = [item for item in raw_list if item % 2 != 0]
print(filtered_list)

print('=============')
# 过滤
new_filtered_list = list(filter(lambda x: x % 2 != 0, raw_list))
print(new_filtered_list)