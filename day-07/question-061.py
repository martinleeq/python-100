"""
问题61
Fibonacci问题
f(0)=0
f(1)=1
f(n)=f(n-1)+f(n-2)
给定n,求f(n)
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
    
    
def fibo2(n):
    """
    非递归的形式
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(n + 1):
            a, b = a + b, a
        return b
    

for i in range(11):
    print(fibo2(i))

