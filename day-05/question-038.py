"""
问题38
生成一个1~10的元组,将前一半的元素输出在一行,后一半的元素输出在另一行
"""


def print_tuple_in_two_lines():
    """
    一个搞混了的知识点: 生成器推导式
    在生成列表的时候,通过推导式生成的直接就是列表,
    但通过小括号推导式生成的对象是一个generator,而我以为这个应该跟列表推导式一样,是一个元组.
    要生成一个元组,可以先生成一个generaotr,再将其转换为元组
    """
    generator = (x for x in range(1, 11))
    a_tuple = tuple(generator)

    print(a_tuple[0: int(len(a_tuple)/2)])
    print(a_tuple[int(len(a_tuple)/2):])


print_tuple_in_two_lines()
