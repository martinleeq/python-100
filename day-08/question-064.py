"""
问题64
输入一个n,通过生成器的方式打印出0 ~ n之间的能被5整除,也能被7整除的数.
"""

def print_5_7(n):
    i = 1
    while i < n:
        i += 1
        if i % 5 == 0 and i % 7 == 0:
            yield i
            

while True:
    n = int(input('Input n:'))
    generator = print_5_7(n)
    for i in generator:
        print(i)