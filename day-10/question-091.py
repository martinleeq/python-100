"""
问题91
输入一个语句,反序输出
"""

def reverse(source):
    result = ''
    count = len(source) - 1
    while(count >= 0):
        result += source[count]
        count -= 1
    return result

def reverse_builtin(source):
    return reversed(source)

def reverse_with_idx(source):
    return source[::-1]

while True:
    raw = input('Input sentence: \n')
    print(reverse(raw))
    print(''.join(reverse_builtin(raw)))
    print(reverse_with_idx(raw))
    