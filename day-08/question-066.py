"""
问题66
从控制台输入一个简单的数学表达式,计算其结果并输出
"""

while True:
    raw = input("Please input the expression:")
    print(eval(raw))