import time


def timethis(func):
    """
    Decorator that reports the execution time.
    """
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper


@timethis
def m_sleep():
    print('sleep 1秒')
    time.sleep(1)
