import time
import threading

def sleep(n):
    time.sleep(n)
    print('sleep %s second' % n)
    return 'money'

t = threading.Thread(target=sleep, args=[3])
#t.setDaemon(True)
t.start()
