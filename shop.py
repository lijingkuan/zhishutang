# coding:gbk

_input = input('���������Ĺ���Ԥ�㣺')
_money = int(_input)
print("�����ʽ��ܶ�Ϊ", _money)

_menu = {'ţ��': 40, '����': 26, 'ƻ��': 5, '����': 3, '����': 1}
_buy_dict = {}

while True:
    _tmp_menu = {}
    print('�����Թ������Ʒ���£�')
    for k, v in _menu.items():
        if _money >= v:
            _tmp_menu[k] = v

    for k, v in _tmp_menu.items():
        print(k, v)

    _buy_item = input('���������������Ʒ��')
    if _buy_item not in _tmp_menu:
        print('�������б��е���Ʒ��')
    else:
        _money = _money - _tmp_menu[_buy_item]
        if _buy_dict.get(_buy_item) == None:
            _buy_dict[_buy_item] = 1
        else:
            cur_num = _buy_dict.get(_buy_item)
            _buy_dict[_buy_item] = cur_num + 1

        if _money > 0:
            print('���Ѿ��������ƷΪ��')
            for k, v in _buy_dict.items():
                print(k, v)

            print('����ʣ����Ϊ��', _money)

    if _money == 0:
        print('������������������Ʒ���£�')
        for k, v in _buy_dict.items():
            print(k, v)
        exit()

filter()