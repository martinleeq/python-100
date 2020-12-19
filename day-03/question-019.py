"""
问题19
name、age、score构成一个元组, 输入一个该元组序列,对该元组进行排序,并输出.
排序优先级为 name > age > score.
"""

arr = []
# arr 中保存着输入的元组序列
while True:
    raw = input()
    if raw:
        arr.append(tuple(raw.split(',')))
    else:
        break
print(arr)

arr.sort(key = lambda x:(x[0], int(x[1]), int(x[2])))
print(arr)