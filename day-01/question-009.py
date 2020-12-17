"""
问题9: 从控制台输入多行语句,将每行语句的字母变成大些然后输出
"""

sentences = []
while True:
    sentence = input()
    if sentence:
        sentences.append(sentence.upper())
    else:
        break

for sentence in sentences:
    print(sentence)
