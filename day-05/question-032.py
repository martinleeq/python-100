"""
问题32
生成一个字典,key为1~20的数字,值为key的平方,然后打印出所有的key.
"""


def generate_print_key():
    dicts = {x: x ** 2 for x in range(1, 21)}
    print(dicts.keys())

generate_print_key()
