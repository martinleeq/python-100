"""
问题31
生成一个字典, key为1 ~ 20的数字, value为该数字的平方
"""

def printDict():
    dicts = {x: x ** 2 for x in range(1, 21)}
    sorted(dicts.items())
    print(dicts)

printDict()
