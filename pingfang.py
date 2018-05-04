def pingfang(x):
    return x*x

ret = []
for i in range(1, 16):
    ret.append(pingfang(i))

print(ret)

# 改成使用map函数，如下：

print(list(map(lambda x:x*x,range(1,16))))
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]
