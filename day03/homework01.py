"""
   练习3： 在一个文件 my.log 中不间断的写入如下内容

 1. 2020-01-01  14:15:16
 2. 2020-01-01  14:15:18
 3. 2020-01-01  14:15:20
 4. 2020-01-01  14:15:22
 5. 2020-01-01  14:15:24
 6. 2020-01-01  14:17:29
 7. 2020-01-01  14:17:31

 每个时间占一行，每隔2秒写入一行
 当程序终止以后，下次启动，要求序号能够衔接继续写
 写的内容每写入一行就要在文件中显示

 提示 ： import time
        sleep()

作业：1. 今天的重点代码能够独立完成
     2. 函数熟悉
     3. 练习3
"""
import time

f = open("my.log", "a+", buffering=1)
count = 1
f.seek(0,0)
for line in f:
    count += 1

while True:
    time.sleep(2)
    data = "%d.%s\n" % (count, time.ctime())
    f.write(data)
    count += 1
f.close()
