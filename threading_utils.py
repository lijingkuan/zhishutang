#coding:gbk

import threading
import time

class FuncThread(threading.Thread):

    def __init__(self, func, *args, **kwargs):
        super(FuncThread, self).__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.finished = False
        self.result = None

    def run(self):
        self.result = self.func(*self.args, **self.kwargs)
        self.finished = True

    def is_finished(self):
        return self.finished

    def get_result(self):
        return self.result

def do_in_thread(func, *args, **kwargs):
    ft = FuncThread(func, *args, **kwargs)
    ft.start()
    return ft

def sleep(n):
    time.sleep(n)
    print('sleep %s second' % n)
    return 'money'

t = do_in_thread(sleep, 2)
time.sleep(2.5)
print("线程是否执行完成：%s" % t.is_finished())
var = t.get_result()
print(var)

#调用方式  do_in_thread(函数名，参数)
#如果想获取结果，就get_result

#基本适用于工作中所有对于线程的需求