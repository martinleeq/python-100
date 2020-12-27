"""
问题95
给定一个字符串s和一个换行的宽度width,对字符串进行换行.
"""

def wrap_for(string, width):
    length = len(string)
    for i in range(length):
        if i % width == 0:
            print()
        print(string[i], end='')
    print()
    

import textwrap
def wrap_builtin(string, width):
    text_arr = textwrap.wrap(string, width)
    for text in text_arr:
        print(text)


while True:
    raw = input('Input string:')
    width = int(input('Input width:'))
    wrap_for(raw, width)
    print('===============')

    wrap_builtin(raw, width)