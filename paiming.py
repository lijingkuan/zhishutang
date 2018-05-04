# 匿名函数，lambda函数相关

#根据分数排名

a = {'lilei':94, 'lily':80, 'lucy':75, 'hanmeimei':90}

print(sorted(list(a.items()), key = lambda x:x[1], reverse=True))