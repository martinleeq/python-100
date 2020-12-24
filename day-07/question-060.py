"""
问题60
f(n)=f(n-1)+100, 当n >0
f(0)=0, n=0
当给定一个n时,计算f(n)的值.
"""

while True:
    n = int(input('Input: '))
    if n == 0:
        print(0)
    else:
        fn, fn1 = 0, 0
        for i in range(1, n + 1):
            fn = fn1 + 100
            fn1 = fn
        print(fn)
