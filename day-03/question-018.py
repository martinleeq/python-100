"""
问题18: 
从控制台输入以逗号分隔的密码序列, 找出其中符合以下条件的密码, 并以逗号风格打印在控制台
密码规则如下:
* 至少有一个小写字母;
* 至少有一个大写字母;
* 至少有一个数字;
* 至少包含一个如下的特殊字符: @、#、$
* 密码长度不小于6;
* 密码长度不大于8
"""

import re

# 基础的密码检查方法
def check_password(password):
    if not password:
        return False

    length = len(password)
    if length < 6 or length > 8:
        return False

    existLower = existUpper = existDigit = False
    for ch in password:
        if ch.isdigit():
            existDigit = True
        elif ch.isupper():
            existUpper = True
        elif ch.islower():
            existLower = True

    return existLower and existUpper and existDigit

# 通过正则表达式进行校验
def check_password_by_reg(password):
    if not password:
        return False

    length = len(password)
    if length < 6 or length > 8:
        return False

    if not re.search('[a-z]', password):
        return False

    if not re.search('[A-Z]', password):
        return False

    if not re.search('[@#$]', password):
        return False

    return True

def check_password_by_reg_all(password):
    if not password:
        return False

    return re.search(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).{6,12}$", password)

passwords = input().split(',')

result = [password for password in passwords if check_password_by_reg(password)]

print(','.join(result))
