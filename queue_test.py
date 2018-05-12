import queue
import time

q = queue.Queue()

for i in range(10):
    q.put(i)

while not q.empty():
    print(q.get())
    time.sleep(0.5)