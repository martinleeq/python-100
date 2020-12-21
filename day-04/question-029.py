"""
问题29
输入两个字符串,将两个字符串拼接起来并输出
"""

def concat(a, b):
    return str(a) + str(b)

def concat_with_join(arr):
    return ''.join(arr)

concat_ops = lambda a, b: str(a) + str(b)

print(concat('basket', 'ball'))
print(concat_ops('basket', 'ball'))
print(concat_with_join(['basket', 'ball']))