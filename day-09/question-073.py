"""
问题73
生成一个包含5个元素的列表,每个元素是100~200之间的随机偶数
"""

import random

a_list = [i for i in range(100,201) if i % 2 == 0]
print(random.sample(a_list, 5))

print('========')
print(random.sample(range(100, 201, 2), 5))