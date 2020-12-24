"""
问题59
控制台输入一个数字n,计算1/2 + 2/3 + 3/4 + ... + n/n+1的值
"""

result = 0

str = int(input())
for i in range(1, str + 1):
    result += i / (i + 1)
print(result)
