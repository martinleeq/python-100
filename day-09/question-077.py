"""
问题77
打印出执行100次1+1的总的时间
"""

import datetime
import time

start = datetime.datetime.now()
for i in range(100):
    x = 1 + 1
end = datetime.datetime.now()

duration = end - start
print('duration = {}'.format(duration.microseconds))

print('==========')
start = time.time()
for i in range(100):
    x = 1 + 1
end = time.time()
duration = end - start
print('duration = {}'.format(duration))
