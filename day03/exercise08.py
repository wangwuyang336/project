"""
   文件偏移量
"""
f = open("/home/tarena/month02-self/day02/file.txt",'wb+')
f.write(b"data.encode\n")
f.flush()
f.seek(-2,2)
data = f.read()
print(data.decode())
f.close()