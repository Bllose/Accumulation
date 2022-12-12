import time
import threading
import asyncio
用async标注方法，显示其为异步执行方法
通过await实现子线程的等待行为
通过asyncio.get_event_loop()下的 run_until_complete()使得主线程一直被阻塞，直到子线程执行完毕
async def hello(cur):
    print('Hello world! (%s)' % threading.currentThread())
    await asyncio.sleep(1)
    print('Hello again! ({0}) - {1}'.format(threading.currentThread(), cur) )
loop = asyncio.get_event_loop()
tasks = [hello(1), hello(2)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
