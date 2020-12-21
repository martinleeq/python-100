"""
问题27
定义一个方法,将数字转换成字符串
"""

def int_2_str(num):
    """
    既可以直接用str()来转换, 也可以通过Lambda表达式
    Labmda表达式可以很方便地进行一些简单的运算,但是比较复杂的, 还是函数比较合适
    """
    print(str(num))


int_2_str_ops = lambda num: print(int(num))

int_2_str(10)
int_2_str_ops(10)
