"""
问题3: 给定一个数字, 生成一个字典, 字典的元素为:
    1. key为数字, value为该数字的平方;
    2. key的范围为1到这个数字
"""

def generate_dict(num):
    if num <= 0:
        return {}

    result = {}
    i = 1
    while num >= i:
        result[i] = i ** 2
        i += 1
    return result

# 遍历操作的一种更方便的方式就是表达式,这是首选的方式,要牢记
def generate_dict_lambda(num):
    if num <= 0:
        return {}

    result = {i : i*i for i in range(1, num + 1)}
    return result

def print_dict(num_dict):
    print(num_dict)


num = int(input())
num_dict = generate_dict(num)
print(num_dict)

num_dict = generate_dict_lambda(num)
print(num_dict)
