#coding:gbk

# 题目：定义一个直线 y=ax + b

def line_conf(a,b):
    def line(x):
        return a*x + b
    return line

y1 = line_conf(2,1)
y2 = line_conf(4,5)

print(y1(5))
print(y2(5))