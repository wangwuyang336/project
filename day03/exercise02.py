"""
   打开文件
   读取文件
   关闭文件
"""
f = open("/home/tarena/month02-self/day02/file.txt",'r')
# f = open("/home/tarena/month02-self/day02/file.txt",'w')
# f = open("/home/tarena/month02-self/day02/file.txt",'a')
# while True:
#     data = f.read(1)
#     if not data:
#         break
#     print(data,end="")
# f.close()

# data = f.readline(15)
# print(data)
# data = f.readline(19)
# print(data)
# f.close()

# data = f.readlines(33)
# print(data)
# f.close()

for line in f:
    print(line,end="")