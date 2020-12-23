"""
问题45
定义一个名为American的类,并在类中声明一个静态方法 printNationality

知识点: 实例方法、类方法、静态方法
"""

class American(object):

    className = 'American'

    def __init__(self) -> None:
        self.instanceName = 'James'

     # def printNationality():
     #   print('printNationality')


    def printAmericanA(self):
        # 实例方法可以调用实例方法
        self.printAmericanB();
        # 实例方法可以调用类方法
        American.printClassMethodA()
        # 实例方法可以调用静态方法
        American.printStaticMethodA()
        print('printAmerican A')

    def printAmericanB(self):
        print('printAmerican B')

    @classmethod
    def printClassMethodA(cls):
        # 类方法可以调用类方法
        American.printClassMethodB()
        # 类方法不能调用实例方法, 实例方法默认会将实例本身作为第一个参数传入实例方法
        # American.printAmericanA()
        
        # 类方法可以调用静态方法
        American.printStaticMethodA()
        print('class method A')
    
    @classmethod
    def printClassMethodB(cls):
        print('Class method B')

    @staticmethod
    def printStaticMethodA():
        print('static method A')

        # 静态方法不能调用实例方法
        # American.printAmericanA()

        # 静态方法可以调用静态方法
        American.printStaticMethodB()

        # 静态方法可以调用类方法
        American.printClassMethodB()

    @staticmethod
    def printStaticMethodB():
        print('static method B')

person = American()
person.printAmericanA()

print('====================')
American.printClassMethodA()

print('====================')
American.printStaticMethodA()
