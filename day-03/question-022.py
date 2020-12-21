"""
问题22: 统计控制台输入的语句中每个词出现的频率,并按照字母顺序输出到控制台
"""

word_dict = {}
words = input().split()

for word in words:
    if not word_dict.get(word):
        word_dict[word] = 1
    else:
        word_dict[word] = word_dict[word] + 1

# 一个重点就是对dict进行排序, 排序时仍然调用sorted方法,传入的是dict.items()
result = sorted(word_dict.items())
print(result)
