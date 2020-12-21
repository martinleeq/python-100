"""
问题25
定义一个类, 在类中声明类的变量和对象的变量
"""

class CustomClass(object):
    """
    类变量属于类对象, 通过类对象对其进行访问
    """
    var = 'Class Variable'
    
    def __init__(self) -> None:
        """ 
        实例变量属于实例,通过实例对其进行访问 
        """
        self.var = 'Instance Variable'
        
print(CustomClass.var)

cc = CustomClass()
print(cc.var)