"""
问题89
定义一个Person类及其两个子类Male和Female,每个类都定义一个getGender方法,返回其gender
"""


class Person(object):
    def __init__(self) -> None:
        self.__gender = 'unknown'
        self.public_gender = 'unkown'
    
    def getGender(self):
        return self.__gender
    
    def getPublicGender(self):
        return self.public_gender


class Male(Person):
    def __init__(self) -> None:
        self.__gender = 'Male'
        self.public_gender = 'Public Male'

    def getGender(self):
        return self.__gender


class Female(Person):
    def __init__(self) -> None:
        self.__gender = 'Female'
        self.public_gender = 'Public Female'
        
    def getGender(self):
        return self.__gender
        

person = Person()
print(person.getGender())

male = Male()
print(male.getGender())

female = Female()
print(female.getGender())

print('=================')
print(male.getPublicGender())
print(female.getPublicGender())