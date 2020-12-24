"""
问题67
给定一个排好序的列表,使用二分查找法找到给出的数,打印其位置信息
"""
def binary_search(target, a_list, start, end): 
    if start == end:
        if a_list[start] == target:
            return start
        else:
            return -1
    
    mid = (int)((start + end) / 2)
    if a_list[mid] == target:
        return mid
    elif a_list[mid] < target:
        return binary_search(target, a_list, mid + 1, end)
    else:
        return binary_search(target, a_list, start, mid)
    
    
while True:
    raw_list = list(map(int, input('Raw List:').split()))
    target = int(input('Target:'))
    print('Target index: ', binary_search(target, raw_list, 0, len(raw_list) - 1))