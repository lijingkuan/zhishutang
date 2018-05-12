_list=[2,3,8,7,9,11,4]
_dict=dict()
for item in _list:
    print(item)
    for k in _dict:
        print(k)
        if k + item == 13:
            _dict.update(k,item)
        else:
            _dict.update(k,0)
for k,v in _dict:
    print(k,v)