"""
问题62
Fibonacci问题
f(0)=0
f(1)=1
f(n)=f(n-1)+f(n-2)
给定n,求f(0),f(1),...,f(n)
"""


def fibo(n):
    """
    递归解决方案
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

result = list(map(fibo, range(11)))
print(result)

result = [fibo(x) for x in range(11)]
print(result)