"""
问题2: 输入一个数,计算并在控制台打印出这个数的阶乘
"""
def is_digital(str):
    try:
        int(str)
        return True
    except (TypeError, ValueError):
        return False


num = '8' 
if not is_digital(num):
    print('the number you input is not digit')
else:
    result = 1
    d = int(num)
    while d > 0:
        result *= d
        d -= 1
    print(f'{num}的阶乘为:{result}')
