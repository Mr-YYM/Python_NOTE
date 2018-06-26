# 这个东东win跑步起来，去bash跑吧！

import os

def child():
    print('这是子进程哦，pid：', os.getpid())
    os._exit(0)

def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            print('子进程开始啦！pid：%s newid：%s' % (os.getpid(), newpid))
            child()
        else:
            print('这是父进程，pid：', os.getpid(), newpid)
        if input() == 'q' : break

parent()