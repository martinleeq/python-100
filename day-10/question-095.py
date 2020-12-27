"""
问题95
给出里参赛运动员的成绩列表,找出其中亚军(runner-up)的成绩
不管有多少个冠军,分数第二的都是亚军.
"""

while True:
    raw = input().split()
    scores = map(int, raw)
    score_list = sorted(list(set(scores)))
    print(score_list)
    print(score_list[-2])