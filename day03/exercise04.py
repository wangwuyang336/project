"""
文件写操作示例
"""
f = open("/home/tarena/month02-self/day02/file.txt", "r+")
n = f.write("AID-2005班级\n")
print("写入了%d个字符"%n)
n = f.write("Python+人工智能\n")
print("写入了%d个字符"%n)
n = f.write("Python\n")
print("写入了%d个字符"%n)
n = f.write("hello world\n")
print("写入了%d个字符"%n)
n = f.write("hello\n")
print("写入了%d个字符"%n)
f.close()
# list01 = ["abc\n","您好\n"]
# n = f.writelines(list01)
# # print("写入了%d个字符"%n)
# f.close()