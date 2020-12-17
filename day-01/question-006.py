"""
问题6: 输入一个逗号分隔的数字序列,作为以下公式的输入, 计算结果并输出
    Q = Square root of [(2 * C * D) / H]
    其中, C = 50, H = 30, D是待输入的数字序列
    求取输出结果

这里关键有两点:
1. 列表推导式
2. 除法的取整
3. 导入时尽量不要导入全部的包
4. 有关四舍五入的问题: Python中是确定的是四舍六入,五平分. 这是由于计算机截取精度决定的.如果精度要求较高,那么使用Decimal.
    round()函数中,五平分,需要根据取舍的位数前的小数奇偶性来判断,奇偶平分.
"""
from math import sqrt

class SquareRootHelper(object):

    def get_input(self):
        arr = input('Please input the number:').split(',')
        self.data = [int(x) for x in arr]


    def calculate(self):
        self.result = [round(sqrt(2 * 50 * x / 30)) for x in self.data]


    def print_result(self):
        print(self.result)
        

if __name__ == "__main__":
    helper = SquareRootHelper()
    helper.get_input()
    helper.calculate()
    helper.print_result()



