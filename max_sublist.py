#coding:gbk

#题目：
#输入：【1, -2, 3, 4， -6, 9， -7, 5】
#求一个列表的子列表之和的最大值

#小技巧：这一类类似算法题都要设定起始值和最大值

#思路：最大值保留历史的最大值，初始值往后相加，如果大于0，继续相加，如果小于0，初始值赋值为0

import sys
"""
求一个列表子列表之和的最大值
条件：列表中是整数，包括正整数和负整数，没有任何顺序
"""

def get_max_value(_list):
    max_value = 0
    temp_value = 0

    for item in _list:
        temp_value += int(item)
        if temp_value < 0:
            temp_value = 0
        if temp_value > max_value:
            max_value = temp_value

    return max_value

if __name__ == '__main__':
    test_list = [1, -2, 3, 4, -6, 9, -7, 5]

    print(get_max_value(test_list))