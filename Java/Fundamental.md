# Java 8 Stream  
Java 集合运算和表达的高阶抽象。 这种风格将要处理的元素集合看做一种流， 流在管道中传输， 并可以在管道的节点上进行处理， 比如筛选， 排序， 聚合等等。  
元素流在管道中经过中间操作(intermediate operation)的处理， 最后由最终操作(terminal operation)得到前面处理的结果。  
+--------------------+       +------+   +------+   +---+   +-------+
| stream of elements +-----> |filter+-> |sorted+-> |map+-> |collect|
+--------------------+       +------+   +------+   +---+   +-------+
- **stream()** 为集合创建串行流  
- **parallelStream()** 为集合创建并行流  
## Foreach  
map方法用于映射每个元素所对应的结果
List<TestVo> testList = new ArrayList<>();
testList.add(new TestVo(11, "Bllose"));
testList.add(new TestVo(22, "Rcedw"));
testList.add(new TestVo(33, "Again"));
testList.add(new TestVo(44, "Forever"));
testList.add(new TestVo(44, "Test"));
testList.add(new TestVo(0, "Empty"));
List<Integer> result = testList.stream().map(TestVo::getId).collect(Collectors.toList());
List<Integer> result_1 = testList.stream().map(TestVo::getId).distinct().collect(Collectors.toList());
List<Integer> result_2 = testList.stream().filter(vo -> vo.getId() > 0).map(TestVo::getId).distinct().collect(Collectors.toList());
System.out.println(result);
System.out.println(result_1);
System.out.println(result_2);
[11, 22, 33, 44, 44, 0]
[11, 22, 33, 44, 0]
[11, 22, 33, 44]
> 操作符号 ```::```  
> 意味着标记一个方法调用规则  
> ```ClassType``` ```::``` ```FunctionName```   
> ```testList.stream().map(TestVo::getId).collect(Collectors.toList())```
> 意味着将_testList_列表中对象调用方法```getId```获取的值组成一个新的列表。  
> ```testList.stream().collect(Collectors.groupingBy(TestVo::getId))```
> 意味着将_testList_对象通过调用方法```getId```获得的值作为关键字，相同的对象组成新的列表，最终组成“关键字”“队列”的新集合。
## Collectors  
将List按照某个值进行分组保存  
List<TestVo> testList = new ArrayList<>();
testList.add(new TestVo(11, "Bllose"));
testList.add(new TestVo(22, "Rcedw"));
testList.add(new TestVo(33, "Again"));
testList.add(new TestVo(44, "Forever"));
testList.add(new TestVo(44, "Test"));
testList.add(new TestVo(0, "Empty"));
Map<Integer, List<TestVo>>  result3 = testList.stream().collect(Collectors.groupingBy(TestVo::getId));
System.out.println(result3);        
{0=[{"id":0,"name":"Empty"}], 33=[{"id":33,"name":"Again"}], 22=[{"id":22,"name":"Rcedw"}], 11=[{"id":11,"name":"Bllose"}], 44=[{"id":44,"name":"Forever"}, {"id":44,"name":"Test"}]}
# lambda express
# java.util.function.Function
```Function<T, R>``` is an **in-built** _functional interface_ introduced in Java 8 in the ```java.util.function``` package. The primary purpose for which ```Function<T, R>``` has been created is for mapping scenarios i.e when an object of a type is taken as input and it is converted(or mapped) to another type. Common usage of Function is in streams where-in the map function of a stream accepts an instance of Function to convert the stream of one type to a stream of another type.
Since ```Function<T, R>``` is a functional interface, hence it can be used as the assignment target for a lambda expression(->) or a method reference(::).  
