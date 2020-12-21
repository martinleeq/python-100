"""
问题23
写一个能计算乘方的方法, 从控制台输入底数(base number)和指数(exponent),并返回幂(power).
"""

def calculate(base, exp):
    return base ** exp


while True:
    base = int(input('Input the base number:\n'))
    exponent = int(input('Input the exponent:\n'))
    power = calculate(base, exponent)
    print("Power of {0}'s {1} is {2}".format(base, exponent, power))
