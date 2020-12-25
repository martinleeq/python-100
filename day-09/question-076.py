"""
问题75
运用zlib包对"hello world!hello world!hello world!hello world!"进行压缩和解压
"""

import zlib

s = 'hello world!hello world!hello world!hello world!'

out = zlib.compress(bytes(s, 'utf-8'))
print(out)
plain = zlib.decompress(out)
print(plain)