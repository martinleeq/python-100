"""
问题88
对列表[12,24,35,24,88,120,155,88,120,155]进行去重,剩下的按照原来的顺序输出.
"""

raw_list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

result = []
for item in raw_list:
    if item not in result:
        result.append(item)

print(result)

