#coding:gbk

#��Ŀ��
#���룺��1, -2, 3, 4�� -6, 9�� -7, 5��
#��һ���б�����б�֮�͵����ֵ

#С���ɣ���һ�������㷨�ⶼҪ�趨��ʼֵ�����ֵ

#˼·�����ֵ������ʷ�����ֵ����ʼֵ������ӣ��������0��������ӣ����С��0����ʼֵ��ֵΪ0

import sys
"""
��һ���б����б�֮�͵����ֵ
�������б����������������������͸�������û���κ�˳��
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