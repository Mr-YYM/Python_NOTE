import time
import os

def count(num):
    for i in range(num):
        time.sleep(1)
        print('[%s] => %s ' % (os.getpid(), i))

for i in range(5):
    pid = os.fork()
    if pid != 0:
        print('Process %d spawned' % pid) # 父进程
    else:
        count(5) # 子进程
        os._exit(0)

print('main exiting')