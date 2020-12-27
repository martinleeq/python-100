"""
问题92
输入一个语句,打印出其中索引为偶数的部分.
"""

while True:
    raw = input('Input sentence:\n')
    result = raw[::2]
    print(result)