"""
问题71
在10~150之间随机生成一个能同时被5和7整除的随机数
"""

import random

count = 10
while count > 0:
    print(random.choice([i for i in range(10, 151) if i % 5 == 0 and i % 7 == 0]))
    count -= 1