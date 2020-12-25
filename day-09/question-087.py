"""
问题87
给出两个列表:[1,3,6,78,35,55]和[12,24,35,24,88,120,155],求交集,交集也为列表
"""

a_list = [1, 3, 6, 78, 35, 55]
b_list = [12, 24, 35, 24, 88, 120, 155]

a_set = set(a_list)
b_set = set(b_list)
inter_set = a_set.intersection(b_set)
inter_list = list(inter_set)
print(inter_list)

inter2_set = a_set & b_set
print(list(inter2_set))