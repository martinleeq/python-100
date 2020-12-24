"""
问题57
读取一个ascii格式的字符串,将其转换成utf-8编码的unicode格式的字符串
"""

s = 'Abcdefg'
u = s.encode('utf-8')
print(u)
