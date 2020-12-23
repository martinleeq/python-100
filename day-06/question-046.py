"""
问题46
定义一个名为American的类以及其子类NewYorker
"""

class American(object):

    def __init__(self):
        print('American')


class NewYorker(American):

    def __init__(self):
        super().__init__()
        print('NewYorker')


newYorker = NewYorker()

