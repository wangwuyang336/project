"""
   字符串与字节串的转换
"""
b1 = b"hello world"
print(type(b1))

b2="你好".encode()
print(b2)
s="hello ，死鬼"
b3=s.encode()
print(b3)
# print(b3.dcode())