"""
问题20
定义一个生成器的类,可以生成0 ~ n内的能被7整除的数
比如: 输入7, 则能输出0, 7
"""

"""
生成器类似于一个可以连续生成对象的函数,每次生成一个对象
它依赖于 yield 的语意, 可以认为暂停当前函数的执行, 并返回 yield 后的值.
如果想获取下一个数, 有两种方式:
1. 调用next(generator)即可
2. generator是iterable的,可以对其进行for循环, 如本例所示.
"""
class GenerateClass(object):

    def by_seven(self, n):
        for i in range(0, n + 1):
            if i % 7 == 0:
                yield i

generateClass = GenerateClass()
generator = generateClass.by_seven(int(input()))

for num in generator:
    print(num)
