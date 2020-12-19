"""
问题10: 输入一个空格分隔的字符串序列,去除重复的字符串, 然后按照字母顺序排序并输出
"""

# 第一步, 从控制台读取以空格分隔的字符串序列,并转换为列表
arr = input().split(' ')

# 第二步, 将arr放入set集合中, 实现去重
aSet = set(arr)

# 第三步, 排序
result = sorted(aSet)

# 第四步, 用空格拼接为一个字符串
str = ' '.join(result)

# 第五步, 打印输出字符串
print(str)


