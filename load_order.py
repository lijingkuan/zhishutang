#coding:gbk

#python解释器加载文件的顺序

var1 = 1
var2 = 2

def test():
    print("执行test")

def test1():
    print("执行test1")

print(var1)
test1()

if __name__ == '__main__':
    print(var2)
    test()

