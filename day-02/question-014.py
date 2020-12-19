"""
问题14: 输入一个字符串,分别计算其中大写字母和小写字母的个数
"""


raw = input()

upperCount = lowerCount = 0

for ch in raw:
    if ch.isupper():
        upperCount += 1
    elif ch.islower():
        lowerCount += 1

# 个人比较喜欢的两种字符串格式化的形式: 通过占位符进行格式化
# 比起和C/C++类似的%s之类的格式化, 这两种格式化使用起来更方便,也不用特别记忆
print(f'Upper Count: {upperCount}, Lower Count: {lowerCount}')
print('Upper Count: {0}\nLower Count: {1}'.format(upperCount, lowerCount))
