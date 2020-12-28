"""
问题98
给定一个日期,计算对应的日期是星期几.
"""

import calendar

while True:
    month, day, year = map(int, input().split())
    
    # 得到的是表示周日 ~ 周六的数字: 0 ~ 6
    week_day = calendar.weekday(year, month, day)
    print(week_day)
    
    print(calendar.day_name[week_day].upper())
    