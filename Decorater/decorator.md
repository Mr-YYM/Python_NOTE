# 装饰器

## 定义

装饰器的作用或者说什么是装饰器，看四段解释

### [① The code ship](https://www.thecodeship.com/patterns/guide-to-python-function-decorators/)

> In the context of design patterns, decorators **dynamically alter the functionality of a function, method or class** **【动态的改变函数或类的功能】**without having to directly use subclasses. 

###  [② Wikipedia](https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Decorators)

> A decorator is any callable Python object that is used to **modify a function, method or class definition.**  

###  [③ Wikipedia](https://en.wikipedia.org/wiki/Decorator_pattern)

>In object-oriented programming, the decorator pattern is a design pattern that allows **behavior to be added to an individual object,** either statically or dynamically, without affecting the behavior of other objects from the same class.【修饰模式，是面向对象编程领域中，一种动态地**往一个类中添加新的行为**的设计模式。】

###  [④ Python之禅](https://foofish.net/python-decorator.html)

> 装饰器本质上是一个 Python 函数或类，它可以让其他函数或类在不需要做任何代码修改的前提下**增加额外功能**，装饰器的返回值也是一个函数/类对象。它经常用于有切面需求的场景，比如：**插入日志**、性能测试、事务处理、缓存、权限校验等场景，装饰器是解决这类问题的绝佳设计。有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码到装饰器中并继续重用。概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。

总结上方的话，简单的理解，装饰器就是给函数添加额外的功能（在不改变原来函数的定义的前提下）

## 基础装饰器

用代码简单的了解装饰器：

```python
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
```

这段代码是我们最后要实现的效果，现在一开始可能看不懂，没关系，我们一步步的了解。

这段代码展示了装饰器的一个使用场景，代码中的装饰器使用是：

```python
@timethis
def m_sleep():
    print('sleep 1秒')
    time.sleep(1)
```

这里我们定义了一个函数，用于sleep 1秒。装饰器在哪，就在他的上方`@timethis` 这样子我们就给`m_sleep()`添加了一个装饰器，即为他们添加了额外的功能，这个功能就是记录函数运行花费的时间。

运行结果：

![](https://codingnote.oss-cn-shenzhen.aliyuncs.com/01.png)

可以看出

该函数本来只是打印输出一串字符并sleep 1秒，然而后边却多了一个计算并打印运算时间的功能。这就是简单的装饰器的应用。

### 如何定义装饰器

```python
def timethis(func):
    """
    Define a Decorator
    """
    def wrapper():
        pass
    return wrapper
```

如上代码所示，要定义一个装饰器，就要定义一个函数，函数名就是装饰器的名字，这个装饰器要接收一个函数作为参数（我们知道，python当中，python函数可以是一个函数对象，因此可以用函数名指向一个函数）

> 一个装饰器就是一个函数，它接受一个函数作为参数**并返回一个新的函数**。

我们继续看代码，定义装饰器之后，我们在它内部继续定义一个函数。最后，装饰器返回了这个函数。该函数（wrapper）返回后，开始执行。

```python
def wrapper():
    start = time.time()
    result = func()
    end = time.time()
    print(func.__name__, end-start)
    return result
```

我们看到，`func()` 这就是被装饰的函数，它在里面开始执行了。`wrapper` 里就定义了装饰器具体做的事情。

## 参考内容

1、https://zh.wikipedia.org/wiki/%E4%BF%AE%E9%A5%B0%E6%A8%A1%E5%BC%8F

2、https://foofish.net/python-decorator.html

3、https://www.thecodeship.com/patterns/guide-to-python-function-decorators/

4、http://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p02_preserve_function_metadata_when_write_decorators.html