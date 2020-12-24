"""
问题53
假设我们有一些形如username@companyname.com的邮箱
请写一段程序来打印给定邮箱的username. username和companyname都是数字组成的.
"""


def extractUsernameFromEmail(email):
    if not email or len(email) == 0:
        raise ValueError('Email can not be None')

    return email.split('@')[0]


while True:
    email = input('Email:')
    print(extractUsernameFromEmail(email))
