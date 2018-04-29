# coding:gbk

_input = input('请输入您的购买预算：')
_money = int(_input)
print("您的资金总额为", _money)

_menu = {'牛肉': 40, '猪肉': 26, '苹果': 5, '橘子': 3, '饮料': 1}
_buy_dict = {}

while True:
    _tmp_menu = {}
    print('您可以购买的商品如下：')
    for k, v in _menu.items():
        if _money >= v:
            _tmp_menu[k] = v

    for k, v in _tmp_menu.items():
        print(k, v)

    _buy_item = input('请输入您购买的物品：')
    if _buy_item not in _tmp_menu:
        print('请输入列表中的商品！')
    else:
        _money = _money - _tmp_menu[_buy_item]
        if _buy_dict.get(_buy_item) == None:
            _buy_dict[_buy_item] = 1
        else:
            cur_num = _buy_dict.get(_buy_item)
            _buy_dict[_buy_item] = cur_num + 1

        if _money > 0:
            print('您已经购买的商品为：')
            for k, v in _buy_dict.items():
                print(k, v)

            print('您的剩余额度为：', _money)

    if _money == 0:
        print('购物结束，您购买的商品如下：')
        for k, v in _buy_dict.items():
            print(k, v)
        exit()

filter()