"""
问题4: 输入一个逗号分隔的数字序列, 根据这些数字,分别生成一个列表和一个元组,并输出.
"""

str = input('Please intput the sequence: ')
arr = str.split(',')

print('this is a list:', arr)
tup = tuple(arr)
print('this is a tuple:', tuple(arr))

arr2 = list(tup)
print('this is a list converted from tuple:', arr2)

# 通过表达式生成的元组是生成器
print('this is a tuple:', (x for x in arr))
