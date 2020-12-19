"""
问题15: 输入一个数字a,计算出a + aa + aaa + aaaa的和
"""

def get_next_num(r, a):
    return r * 10 + a

a = int(input("Please input number: 'a'"))
b = int(input("Please input time: 'b'"))

total = start = 0
for i in range(b):
    start = get_next_num(start, a)
    total += start
print('The total is {}'.format(total))

