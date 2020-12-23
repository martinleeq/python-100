"""
问题39
给定一个元组,由此生成一个新的元组,其元素为原来元组中为偶数的元素
"""

def print_another_tuple():
    generator = (x for x in range(1, 11))
    pre_tuple = tuple(generator)

    new_generator = (x for x in pre_tuple if x % 2 == 0)
    new_tuple = tuple(new_generator)
    print(new_tuple)


print_another_tuple()        
