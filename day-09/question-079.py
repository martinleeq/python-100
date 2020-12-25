"""
问题79
根据主语、动词、对象列表,生成所有可能的语句.
主语: I, You
动词: Play, Love
对象: Hockey, Football
"""

subjects = ['I', 'You']
verbs = ['Play', 'Love']
objects = ['Hockey', 'Football']

for subject in subjects:
    for verb in verbs:
        for object in objects:
            print(f'{subject} {verb} {object}')

print('===============')
import itertools
sentences = [subjects, verbs, objects]
a_list = list(itertools.product(*sentences))
for item in a_list:
    print(item)
