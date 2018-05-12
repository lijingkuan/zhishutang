#coding:gbk
f = open('namelist.txt','r')
content = f.readlines()
f.close()

for it in content:
    print(it.split())

while True:
    _input = input("输入查询的信息：")
    if _input=='all':
        for item in content:
            print(item,end='')
    elif _input == 'q':
        exit()
    elif '-' in _input:
        a,b = _input.split('-')



a,b = _input.split('-')
#print(a)
#print(b)
#print(content)