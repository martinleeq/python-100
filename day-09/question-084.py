"""
问题84
生成一个3 * 5 * 8的三维数组,元素都为0
"""

a_list = [0 for i in range(3)]
print(a_list)
print('================')

a_list = [[0 for j in range(5)] for i in range(3)]
print(a_list)
print('================')

a_list = [[[0 for k in range(8)] for j in range(5)] for i in range(3)]
print(a_list)
print('================')