"""
问题75
随机生成一个7到15之间的数字
"""

import random

print(random.randrange(7, 16))
print(random.choice(range(7, 16)))
print(random.uniform(7, 16))