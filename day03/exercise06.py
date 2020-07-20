"""
   with语句块 打开文件
"""
with open("/home/tarena/month02-self/day02/file.txt",'rb+') as f:
    data = f.read(5)
    print(data.decode())
    f.write(b"hahdudjjjklja")