"""
问题16: 输入一个逗号分隔的数字序列, 去掉其中的奇数, 并对偶数执行平方运算, 并输出
"""

raw = input().split(',')

result = [str(int(i) ** 2) for i in raw if int(i) % 2 != 0]
print(','.join(result))
