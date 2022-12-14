``` SELECT VERSION(); ```
**与锁表有关的语句**  
show OPEN TABLES where In_use > 0;
show status like '%lock%';
show processlist;
SELECT * FROM INFORMATION_SCHEMA.INNODB_LOCKS;
SELECT * FROM INFORMATION_SCHEMA.INNODB_LOCK_WAITS;
```show OPEN TABLES where In_use > 0;```  
| Database | Table | In\_use | Name\_locked |
| :--- | :--- | :--- | :--- |
| ExampleExample | Example\_attachment\_t | 8 | 0 |
| ExampleExample | Example\_return\_apply\_detail\_t | 8 | 0 |
| ExampleExample | sequence | 1 | 0 |
| ExampleExample | Example\_guest\_association\_t | 2 | 0 |
| ExampleExample | Example\_device\_bom\_t | 8 | 0 |
| ExampleExample | Example\_reverse\_positions\_t | 8 | 0 |
| ExampleExample | Example\_return\_apply\_t | 9 | 0 |  
```show status like '%lock%';```
| Variable\_name | Value |
| :--- | :--- |
| Com\_lock\_tables | 0 |
| Com\_unlock\_tables | 0 |
| Handler\_external\_lock | 2 |
| Innodb\_row\_lock\_current\_waits | 0 |
| Innodb\_row\_lock\_time | 25316234 |
| Innodb\_row\_lock\_time\_avg | 8441 |
| Innodb\_row\_lock\_time\_max | 301522 |
| Innodb\_row\_lock\_waits | 2999 |
| Key\_blocks\_not\_flushed | 0 |
| Key\_blocks\_unused | 319650 |
| Key\_blocks\_used | 16 |
| Locked\_connects | 0 |
| Performance\_schema\_locker\_lost | 0 |
| Performance\_schema\_metadata\_lock\_lost | 0 |
| Performance\_schema\_rwlock\_classes\_lost | 0 |
| Performance\_schema\_rwlock\_instances\_lost | 0 |
| Performance\_schema\_table\_lock\_stat\_lost | 0 |
| Qcache\_free\_blocks | 1 |
| Qcache\_total\_blocks | 1 |
| Table\_locks\_immediate | 1020295 |
| Table\_locks\_waited | 0 |  
```show processlist;```  
| Id | User | Host | db | Command | Time | State |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2287856 | ExampleExample | 10.242.118.143:62948 | ExampleExample | Query | 339 | updating |
| 2287857 | ExampleExample | 10.116.198.111:60692 | ExampleExample | Query | 89 | Sending data |
| 2287858 | ExampleExample | 10.116.198.111:60754 | ExampleExample | Sleep | 1507 |  |
```SELECT * FROM INFORMATION_SCHEMA.INNODB_LOCKS;```  
## Function
``` show function status; ```
## Procedure
``` show procedure status; ```
``` ALTER TABLE table_name DROP PRIMARY KEY; ```   
- 查询表信息  
use information_scheam;
select * from tables where table_schema = "db_name" and table_name = "table_name1";
## Column  
- 查看表下所有字段  
``` SHOW FULL COLUMNS FROM database.table_name; ```  
MySQL 下只能针对表中所有字段进行信息输出。  
如果需要获取部分字段信息， 需要做额外处理。
 全局层 - mysql.user  
 数据库层 - mysql.db & mysql.host  
 表层  -  mysql.table_priv
 列层  -  mysql.columns_priv  
 子程序  -  mysql.procs_priv
### LIMIT \[offset,\] rows | LIMIT rows OFFSET offset
> 这里offset相当于游标， 指向起始位置， 比如：  
> ```SELECT *  FROM orange LIMIT 5; -- 检索前5条记录(1~5)```  
> ```SELECT * FROM orange LIMIT 0, 5;```  
> ```SELECT * FROM table_name LIMIT 10,15; -- 检索记录 11~25```
# 特性，技巧  
- quenece  
MySQL中并没有提供Oracle中独立的队列功能。 如果需要实现队列功能， 则需要通过 Function + table 的形式进行实现。  
但是， MySQL的```FUNCTION``` 不允许显性或隐性地出现 ```commit```功能。 这就出现一种问题：  
在其他语言调用过程中， 同一个 translation 中， 如果需要循环获取自增数， 自增 FUNCTION 将无法达到目的。  
因为每次自增行为都是脏数据。  
而该情况在 LOOP 语句中不存在。  即在存储过程中直接使用自增函数， 可以达到获取自增数列的目的。
> ``` GRANT 权限 ON 数据库对象 TO 用户 ```  
> ``` SQL  
> create user user_name@'%' identified by 'password'; 
> grant select,insert,update,delete on test.t_m_user to user_name@'%';
1. ``` GRANT create view ON database_name.'*' TO user_name@'%'; ```
2. ``` GRANT show view ON database_name.'*' TO user_name@'%'; ```
### [42000][1133] Can't find any matching row in the user table
本质上是由于语句执行过程中无法找到匹配的角色信息， 而该角色信息保存在  
``` SELECT Host, User from mysql.user; ```  
例如， 在该条语句中``` GRANT CREATE VIEW ON abc.* TO ABC@'%'; ```出现异常。
是因为__user__表中的用户为  
 Host | User 
 ---- | ----
 % | abc  
 修改命令为``` GRANT CREATE VIEW ON abc.* TO abc@'%'; ```执行正常。
- 查看执行进程  
SHOW PROCESSLIST;
| Id | User | Host | db | Command | Time | State | Info |  
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1664720 | user_name | 10.244.217.140:38938 | db_name | Sleep | 92 | "" |  |
| 1664904 | user_name | 10.244.217.140:43470 | db_name | Sleep | 3 | "" |  |
| 1664936 | user_name | 10.244.217.140:44550 | db_name | Sleep | 450 | "" |  |
| 1664991 | user_name | 10.242.118.143:59626 | db_name | Query | 292 | updating | /* ApplicationName=DataGrip 2020.1 */ UPDATE db_name.table_name t SET t.store_type = '7' WHER |
| 1664992 | user_name | 10.244.217.140:45684 | db_name | Sleep | 270 | "" |  |
| 1664993 | user_name | 10.244.217.140:45686 | db_name | Sleep | 270 | "" |  |
| 1664994 | user_name | 10.244.217.140:45688 | db_name | Sleep | 270 | "" |  |
| 1664995 | user_name | 10.244.217.140:45690 | db_name | Sleep | 270 | "" |  |
| 1664996 | user_name | 10.244.217.140:45692 | db_name | Sleep | 270 | "" |  |
| 1664997 | user_name | 10.244.217.140:45694 | db_name | Sleep | 270 | "" |  |
| 1664998 | user_name | 10.244.217.140:45696 | db_name | Sleep | 270 | "" |  |
| 1665023 | user_name | 10.242.118.143:59726 | db_name | Query | 191 | updating | /* ApplicationName=DataGrip 2020.1 */ UPDATE db_name.table_name t SET t.store_type = '7' WHER |
| 1665065 | user_name | 10.242.118.143:59964 | db_name | Query | 0 | starting | /* ApplicationName=DataGrip 2020.1 */ SHOW PROCESSLIST |
