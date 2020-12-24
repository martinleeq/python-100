"""
问题68
使用随机模块生成一个10~100之间的随机浮点数
"""

import random

for i in range(10):
    print(random.random() * 100)
    
print('=======================')
    
for i in range(10):
    print(random.uniform(10, 100))