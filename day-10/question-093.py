"""
问题93
打印出[1, 2, 3]所有置换的组合.
"""

import itertools

arr = [1, 2, 3]
print(list(itertools.permutations(arr)))