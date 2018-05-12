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

def a():
    time.sleep(5)
    print('a:done')

t =  do_in_thread(a)
t.join()

# join()不加参数，会先执行a函数，再执行最后的print函数，即主线程等线程t执行完之后再执行
# join(3),则线程阻塞主线程3秒，3秒后执行print函数，函数a的输出在后面

print("测试join")