- 如果已经拥有一个数组对象， 想在要将另外一个数组中的一部分/全部拷贝过来。那么使用：  
System.arraycopy(sourceArray, position, destinationArray, position, length);
- 如果想从已有的数组中，直接全量拷贝过来， 那么使用clone:  
// rows 行数由某处确定，二维数组我们仅初始化行数，每一行的数组由数据源直接拷贝过来
int[][] matrix = new int[rows][];  
for(int i = 0; i < rows; i ++) {
  // sourceArray 从某个数据源获取
  matrix[i] = sourceArray.clone();
[stackoverflow相关问题解答](https://stackoverflow.com/questions/46145826/why-clone-is-the-best-way-for-copying-arrays)
