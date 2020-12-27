"""
问题90
输入一个字符串,计算其中每个字符的数量
"""

while True:
    raw = sorted(input("Please input string: \n"))
    print('{} characters are inputted'.format(len(raw)))
    dict = {}
    
    for ch in raw:
        if ch in dict:
            dict[ch] += 1
        else:
            dict[ch] = 1
    
    print(dict)