"""
问题65
请写一个断言来判断列表[2,4,6,8]中的元素都是偶数
"""

a_list = [2,4,6,8, 9]
for item in a_list:
    assert item % 2 == 0, "{} is not even number.".format(item)
    
print('All the elements are even numbers.')