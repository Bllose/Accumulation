当我们需要遍历一个Map时，经常会使用如下代码：  
Map<TYPE, TYPE> map = target.streat().collect(Collectors.groupingBy(vo::key));
for(TYPE key: map.keySet()){
  TYPE value = map.get(key);
这样写的最大好处在于它非常符合人们常用的思维习惯。可惜它性能不佳，修改为如下形式可以提高1.25倍的性能: 
Map<TYPE, TYPE> map = target.streat().collect(Collectors.groupingBy(vo::key));
Set<Map.Entry<TYPE, TYPE>> entries = map.entrySet();
Iterator<Map.Entry<TYPE, TYPE>> iterator = entries.iterator();
while(iterator.hasNext()){
  theEntry = iterator.next();
  TYPE value = theEntry.getValue();
  TYPE key = theEntry.getKey();
