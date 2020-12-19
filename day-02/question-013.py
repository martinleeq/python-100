"""
问题13: 输入一个句子,算出其中字母和数字的个数
"""

# 最简便的判断输入字符类型方式就是内置的方法:
# isdigit: 是否是数字
# isalpha: 是否是字母
# isalnum: 是否是数字或字母
# islower: 是否都是小写字母
# isupper: 是否都是大写字母
# istitle: 是否是首字母大写,像标题
# isspace: 所有字符是否都是空白字符、\t、\n、\r
raw = input()

alpha = 0
digital = 0
for ch in raw:
    if ch.isdigit():
        digital += 1
    elif ch.isalpha():
        alpha += 1

print(f'LETTERS: {alpha}, DIGITALS: {digital}')
