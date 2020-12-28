"""
问题97
给定一个整数n,打印Rangoli序列.
比如:n=3时, 输出:
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
"""

import string

def print_rangoli(size):
    n = size
    alph = string.ascii_lowercase
    width = 4 * n - 3

    ans = []
    for i in range(n):
        left = '-'.join(alph[n - i - 1:n])
        mid = left[-1:0:-1] + left
        final = mid.center(width, '-')
        ans.append(final)

    if len(ans) > 1:
        for i in ans[n - 2::-1]:
            ans.append(i)
    ans = '\n'.join(ans)
    print(ans)

    while True:
        n = int(input())
        print_rangoli(n)
        print('===============')
