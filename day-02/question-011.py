"""
问题11: 从控制台输入一个以逗号分隔的四位二进制数, 判断是否能被5整除. 将能被5整除的二进制数以逗号分隔输出
"""

# 第一步, 将输入的内容转换为列表
raw = input().split(',')

result = []

# 第二步, 遍历列表中的元素,判断其是否能被5整除,如果可以,则放入结果列表
for str in raw:
    num = int(str, 2)
    if num % 5 == 0:
        result.append(str)

# 第三步, 拼接并输出
print(','.join(result))

