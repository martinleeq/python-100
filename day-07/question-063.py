"""
问题63
给定一个n,使用生成器的方式生成0 ~ n的偶数
"""

def even_number(n):
    i = 0
    while i < n:
        i += 1
        if i % 2 != 0:
            continue
        yield i
  
values = []
generator = even_number(10)
for i in generator:
    print(i)