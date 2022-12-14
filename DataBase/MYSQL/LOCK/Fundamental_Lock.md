- 当使用简单```SELECT```语句时， 即不加锁， 也不会被其他锁干扰， 直接搜出脏数据。
# 查询于锁有关的线程信息
show variables like 'autocommit';
show full PROCESSLIST;
select * from information_schema.INNODB_LOCKS;
select * from information_schema.innodb_lock_waits;
**制造锁现场**
set autocommit = OFF; 
start transaction;
select * from Example_return_apply_t where apply_id = 1143 for update;
在另外一个线程执行  
select * from Example_return_apply_t where apply_id = 1143 LOCK IN SHARE MODE;
| lock\_id | lock\_trx\_id | lock\_mode | lock\_type | lock\_table | lock\_index | lock\_space | lock\_page | lock\_rec | lock\_data |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1966905:719:3:10 | 1966905 | S | RECORD | \`ExampleExample\`.\`Example\_return\_apply\_t\` | PRIMARY | 719 | 3 | 10 | 1143 |
| 1966904:719:3:10 | 1966904 | X | RECORD | \`ExampleExample\`.\`Example\_return\_apply\_t\` | PRIMARY | 719 | 3 | 10 | 1143 |
# 指定锁类型的查询语句  
排他锁:写锁:X锁  
select * from tableName where columnName = searchValue for update;
该语句可以保证查询到的值为最后更新的值， 但如果有update语句没有提交，将要等待。  
共享锁:读锁:S锁
select * from tableName where columnName = searchValue LOCK IN SHARE MODE;
该语句如果有update语句没有提交， 也时需要等待的， 最终会查询到update之后的结果。  
select * from tableName where columnName = searchValue;
普通的查询语句， 不会收到update的锁影响， 会查出脏数据。
