import multiprocessing
import time

def job(q, n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    q.put(sum)


def mulp(n):
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=job, args=(q,n))
    p2 = multiprocessing.Process(target=job, args=(q,n))
    p1.start()
    p2.start()
    print(q.get() + q.get())

def normal(n):
    sum = 0
    for i in range(1,n+1):
        sum += i

    for i in range(1,n+1):
        sum += i

    print(sum)

if __name__ == '__main__':
    t1 = time.time()
    normal(1000000)
    t2 = time.time()
    print('normal:', t2-t1)

    t1 = time.time()
    mulp(1000000)
    t2 = time.time()
    print('multiprocess:', t2-t1)
