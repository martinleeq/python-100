"""
问题74
生成一个包含5个元素的列表,每个元素是1~1000之间的能同时被5和7整除的随机数
"""

import random

a_list = [i for i in range(1, 1001) if i % 35 == 0]
print(random.sample(a_list, 5))
