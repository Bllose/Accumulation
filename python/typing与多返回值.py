from typing import Tuple, List, AnyStr
通过 typing 指定类型， 类似于java的范式
直接将多个结果返回出去， 类似于 GO 的机制
这里有一点有待考究， 返回值认定为 Tuple一个对象， 在定义时， 该Tuple拥有两个List，
对于使用者而言， 直接拿两个对象就能直接跳过 Tuple， 拿到里面的两个 List
def getMutiTuple() -> Tuple[List[AnyStr], List[AnyStr]]:
    result1:List[String] = ["Bllose", "Chen"]
    result2:List[String] = ["Rcedw", "Xi"]
    return result1, result2
result1, result2 = getMutiTuple()
for cur in result1:
    print(cur)
print(" ")
for cur in result2:
    print(cur)
