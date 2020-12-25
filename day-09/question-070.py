"""
问题70
在0~10之间生成一个偶数的随机数
"""

import random

count = 10
while count > 0:
    print(random.choice([i for i in range(11) if i % 2 == 0]))
    count -= 1