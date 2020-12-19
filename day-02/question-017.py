"""
问题17: 银行账户计算, D代表储蓄, W代表取出. 从控制台输入多条账号操作, D或者W,计算最终的账户数额
"""

result = 0
while True:
    ops = input().split()
    if ops[0] == 'D':
        result += int(ops[1])
    elif ops[0] == 'W':
        result -= int(ops[1])
    else:
        break

print(f'result={result}')
