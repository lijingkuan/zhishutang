#coding:gbk

class MysqlOpers:
    def __init__(self):
        """连接数据库"""
        print('do __init__')

        #伪代码
        #self.db = MySQLdb.connect

    def select(self):
        print(111)
        pass

    def insert(self):
        pass

# 自己封装的MySQL连接模块经常如下：
# 每次执行操作都需要连接数据库
# dba = MysqlOpers()
# dba.select()
# dba = MysqlOpers()
# dba.insert()

# 在监控类应用中，可以将MySQL连接作为类属性

class B:
    a = MysqlOpers()

#    def __init__(self):
#        self.a = MysqlOpers()

    def test(self):
        print(id(self.a))

if __name__ == '__main__':
    b = B()
    b.test()
    b = B()
    b.test()

# 两次输出相同，是相同的对象，因为内存地址相同
# 如果将a = MysqlOpers()写在init函数里，则每次b = B()生成的a是不同的对象

# 如果建立mysql连接的对象作为类属性的话，好处：
# 多次调用类方法，只建立一个mysql连接对象
# class A 的init只执行一次
