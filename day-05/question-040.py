"""
问题40
输出一个字符串,如果是'YES'或者'Yes', 'yes',则打印出yes,否则打印出no
"""

def verify_yes():
    while True:
        x = input('Input your string:')
        if x == 'YES' or x == 'Yes' or x == 'yes':
            print('yes')
        else:
            print('no')

verify_yes()
