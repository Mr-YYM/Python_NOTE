import multiprocessing
import os
import time

def job():
    while 1:
        print('Process 【%s】running' % os.getpid())
        time.sleep(1)

if __name__ == '__main__':
    print('main 【%s】running' % os.getpid())
    p1 = multiprocessing.Process(target=job)
    p1.start()
    # p1.join()
    while 1:
        print('main 【%s】running' % os.getpid())
        time.sleep(0.1)