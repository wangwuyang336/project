"""
练习1：使用input输入一个单词，打印出这个单词的解释
，如果没有这个单词则打印"没有找到该单词"

提示：
    * 每个单词占一行
    * 单词与解释之间有空格
    * 单词按照从小到大排列
"""
word = input("请输入一个单词:")
f = open("dict.txt")
for line in f:
    w = line.split(' ',2)
    if w[0] > word:
        print("没有该单词")
        break
    elif w[0] == word:
        print(w[-1].strip())
        break
else:
    print("没有找到该单词")
f.close()