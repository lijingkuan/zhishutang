import queue
import threading

q = queue.Queue()

class Con(threading.Thread):

    def __init__(self,q):
        self.q = q

    def run(self,q)\
        if q.get() == 'finish':
            print('byebye')
            exit(1)

class Pro(threading.Thread):

    def __init__(self,q):
        self.q =q

    def run(self,q):
        q.put()