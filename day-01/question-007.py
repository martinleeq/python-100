"""
问题7: 输入两个数x和y,构造一个x * y的二维列表, 其中x, y的元素的值为x * y
"""

x = int(input('x='))
y = int(input('y='))
# 二维数字的外循环,即x的循环,表示二维数字有几个一维数组, 内循环表示每个一维数组有几个元素
arr = [[a * b for a in range(y)] for b in range(x)]

print(arr)
