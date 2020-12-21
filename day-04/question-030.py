"""
问题30
输入两个字符串, 输出其中长度更长的一个. 如果两个长度相同, 则将两个字符串换行输出
"""

def output_more_length(a, b):
    diff = len(a) - len(b)
    if diff > 0:
        print(a)
    elif diff < 0:
        print(b)
    else:
        print(a)
        print(b)
a = 'Hello'
b = 'AHiiii'

output_more_length(a, b)
