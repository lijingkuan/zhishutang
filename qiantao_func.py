def test(m,n):

    def test1():
        print("haha")
        return m+n

#    return test1()

test(8,9)
# 在不加return test1（）的情况下，本来我以为会输出“haha”
# 结果什么都没输出
# 原因是，只有在被调用时才会去执行
# 否则，只会运行到def test1()这一步，把函数注册一下
# 函数体不会执行的
# 只有函数被调用时，才会执行函数体的内容
# 子函数也是如此！！！