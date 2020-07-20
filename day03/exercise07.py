"""
   缓冲区演示
"""
f = open("/home/tarena/month02-self/day02/file.txt",'wb',buffering=10)
while True:
    data = input(">>")
    # if data == "":
    if not data:
        break
    f.write(data.encode())
    # f.flush()
f.close()