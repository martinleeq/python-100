"""
问题12: 输入一个数字,判断这个数字每一位是否都是偶数的数字
"""


# 这是纯数学的计算,十进制的方式判断每一位是否能被2整除
# 还可以将数字转换成字符串,对字符串的每一位,判断是否能被2整除,可能更简单
def is_all_digit_even(num):
    a = num % 10
    b = (int)(num / 10)
    print(f'num={num},a={a}, b={b}')
    while b > 10:
        if a % 2 != 0:
            return False
        a = b % 10
        b = (int)(b / 10)

    return a % 2 == 0 and b % 2 == 0

result = []

while True:
    raw = int(input())
    print(is_all_digit_even(raw))

