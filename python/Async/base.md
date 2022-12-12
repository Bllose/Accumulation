# [Coroutines](https://docs.python.org/3/library/asyncio-task.html)
直接调用```coroutine```类型的方法是不对的，这个方法不会真的执行。```asyncio```提供了三种方式用于调用```coroutine```方法，使其真正地执行。  
### 针对顶层入口(Top-level entry point)
>>> import asyncio
>>> async def main():
...     print('hello')
...     await asyncio.sleep(1)
...     print('world')
>>> asyncio.run(main())
### Awaiting on a coroutine
``` Python
import asyncio
import time
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
async def main():
    print(f"started at {time.strftime('%X')}")
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f"finished at {time.strftime('%X')}")
asyncio.run(main())
### 以任务为维度
延续上文中的 ```say_after```方法:
``` Python
async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))
    task2 = asyncio.create_task(
        say_after(2, 'world'))
    print(f"started at {time.strftime('%X')}")
    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")
# Awaitables
我们将能正确写入```await```表达式的对象称之为**awaitable对象**。大部分```asyncio APIs```都被设计为```awaitable```类型。  
目前主要有三种```awaitable对象```: ```coroutines```, ```Tasks```, and ```Futures```.
### Coroutines  
Python coroutines are awaitables and therefore can be awaited from other coroutines:  
``` Python
import asyncio
async def nested():
    return 42
async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested()
    # Let's do it differently now and await it:
    print(await nested())  # will print "42".
asyncio.run(main())
对于术语```coroutine```，有两个近似的概念，不要弄混了:
- 一个```coroutine```方法: 就是指一个被```async def```前缀定义的方法
- 一个```coroutine```对象: 指通过调用一个```coroutine```方法而返回的对象。
```Tasks```用来运行一些预设好的异步执行的待办任务。
当一个```coroutine```被类似于```asyncio.create_task()```方法封装后，它就成为一个准备完成的待办任务。  
``` Python
import asyncio
async def nested():
    return 42
async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())
    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await task
asyncio.run(main())
# Future  
```Future```是一个底层(low-level)的 _awaitable_ 对象，用来显示一个异步操作的**最终结果**（eventual result）.
一般情况下，我们不需要在产品级代码中使用```Future```对象。
```Future```对象可以被```await```语法调用，这些对象有时是发布在一些包里或者是```asyncio APIs```中:  
``` Python
async def main():
    await function_that_returns_a_future_object()
    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
下面有一个很好的[例子](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor)，用来演示底层返回```Future```对象的方法。  
