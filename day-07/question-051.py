"""
问题51
写一个方法用于计算5 / 0, 并用try/except捕获异常
"""

def devide(x, y):
    try:
        print(x / y)
        print('Division ok.')
    except ZeroDivisionError as er:
        print(er)
    except Exception as der:
        print(der)
    finally:
        print('Division finally.')
        

while True:
    x = int(input())
    y = int(input())
    devide(x, y)