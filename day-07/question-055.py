"""
问题55
写一段程序,当传入一段以空格分隔的字符串时,打印只有数字的字符串
"""


import re


def is_number(s):
    return s.isdigit()


def print_digital(string):
    str_list = string.split()
    for s in str_list:
        if is_number(s):
            print(s, end=',')


def print_digital_re(string):
    # 正则表达式模式用r''表示,\b表示空格,这里表示前后都是空格
    pattern = r'\b\d+\b'
    ans = re.findall(pattern, string)
    print(ans)


print_digital('hello 123 g 3 as3c 3a.')

print_digital_re('hello 123 g 3 as3c 3a.')
