_list = [1,'aa','123','test',8,9,7]

def filter_str(item):
    if isinstance(item,str):
        return False
    else:
        return True

ret = []
rst = filter(filter_str, _list)
for item in rst:
    ret.append(item)

print(ret)