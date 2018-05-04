var = 12

def change_var():
#    global var
    var = 13
    return var

print(change_var())
print(var)
"""
输出结果：
把global注释掉，输出 13,12
不注释global，输出13,13
"""