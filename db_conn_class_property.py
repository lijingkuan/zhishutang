#coding:gbk

class MysqlOpers:
    def __init__(self):
        """�������ݿ�"""
        print('do __init__')

        #α����
        #self.db = MySQLdb.connect

    def select(self):
        print(111)
        pass

    def insert(self):
        pass

# �Լ���װ��MySQL����ģ�龭�����£�
# ÿ��ִ�в�������Ҫ�������ݿ�
# dba = MysqlOpers()
# dba.select()
# dba = MysqlOpers()
# dba.insert()

# �ڼ����Ӧ���У����Խ�MySQL������Ϊ������

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

# ���������ͬ������ͬ�Ķ�����Ϊ�ڴ��ַ��ͬ
# �����a = MysqlOpers()д��init�������ÿ��b = B()���ɵ�a�ǲ�ͬ�Ķ���

# �������mysql���ӵĶ�����Ϊ�����ԵĻ����ô���
# ��ε����෽����ֻ����һ��mysql���Ӷ���
# class A ��initִֻ��һ��
