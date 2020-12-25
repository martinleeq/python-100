"""
问题72
生成一个包含5个元素的列表,每个元素是100~200之间的随机数
"""

import random

a_list = []
for i in range(5):
    a_list.append(random.choice(range(100,201)))
print(a_list)

print('==================')
a_list.clear()
print(random.sample(range(100,201), 5))