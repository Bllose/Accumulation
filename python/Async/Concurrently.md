_awaitable_ asyncio.**gather\(** \*aws, return_exceptions=False **\)**  
通过执行 _aws_ 队列中的```awaitable```对象，使得他们同时运行。
只要在 _aws_ 队列中，任意一个对象是```coroutine```，那么该方法就会将他们当做```Task```运行。  
当所有任务都成功执行完毕，他们的返回值会聚合成一个列表，以一个队列结果的形式返回出来。 这些结果的顺序，与其方法在 _aws_ 队列位置有关。
``` Python
import asyncio
async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f
async def main():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    print(L)
asyncio.run(main())
# Expected output:
#     Task A: Compute factorial(2), currently i=2...
#     Task B: Compute factorial(3), currently i=2...
#     Task C: Compute factorial(4), currently i=2...
#     Task A: factorial(2) = 2
#     Task B: Compute factorial(3), currently i=3...
#     Task C: Compute factorial(4), currently i=3...
#     Task B: factorial(3) = 6
#     Task C: Compute factorial(4), currently i=4...
#     Task C: factorial(4) = 24
#     [2, 6, 24]
