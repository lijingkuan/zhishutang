#coding:gbk

#题目要求：
#删除列表中的字符串的项
_list = [1,'aa','123','test',8,9,7]

for item in _list:
    if isinstance(item,str):
        _list.remove(item)

print(_list)

#输出结果为 [1, '123', 8, 9, 7]
#其中‘123’为字符串却未被删除，什么原因？

#将程序改造一下
_list = [1,'aa','123','test',8,9,7]

for index,item in enumerate(_list):
    print(index, item)
    if isinstance(item,str):
        _list.remove(item)

print(_list)

#输出结果为：
# 0 1
# 1 aa
# 2 test
# 3 9
# 4 7
# [1, '123', 8, 9, 7]

#原因解释：
#初始列表为[1,'aa','123','test',8,9,7]
# 当程序执行到第二项'aa'后，删除了列表中的‘aa’，此时列表变为[1,'123','test',8,9,7]，
# ‘123’变成了新列表中的第二项
# 因此接下来检查第三项的时候，就把原来的第三项跳过去了，因此字符串'123'没有被删掉

#=============================================================
#结论：不能在循环遍历中删除列表本身的元素，否则可能会导致错乱
#=============================================================

#=============================================================
#解决思路：
#再拷贝一个对象，这个对象和原来的对象是两个不同内存地址的两个对象
#遍历新的对象，删除原来的对象元素
#=============================================================


#=============================================================
#解决办法：使用深拷贝
#=============================================================

import copy

_list = [1,'aa','123','test',8,9,7]

new_list = copy.deepcopy(_list)

for item in new_list:
    if isinstance(item,str):
        _list.remove(item)

print(_list)

#输出结果为[1, 8, 9, 7]
