``` SQL  
select * from dba_sequences where sequence_owner='sequenceOwner';
**获取当前schema下队列信息**  
select * from user_sequences;
| SEQUENCE_NAME |MIN_VALUE |MAX_VALUE | INCREMENT_BY |CYCLE_FLAG |ORDER_FLAG |CACHE_SIZE |LAST_NUMBER |
| --- |--- |--- |--- |--- |--- |--- |--- |
| CHECK_NO_S |10000 |99999 |20 |Y |N |0 |12093 |
| CHANGE_PRODUCT_CFG_S |1 |1000000000000 |1 |Y |N |100 |2819 |
| CHECK_S |1000 |9999999999999999999999999999 |1 |N |Y |0 |104623 |
| API_LOG_S |100001 |9999999999999999999999999999 |1 |N |N |0 |2335231 |    
- CACHE_SIZE: 内存中缓存sequence队列深度（share pool）,设置过小时可能出现 row cache lock的等待事件。
- ORDER_FLAG: 是否按顺序生成。 默认为N， 实际使用中，在队列定义范围内依然是按照 ```INCREMENT_BY``` 进行递增。 具体有什么含义有待验证。
create sequence sequence_name
increment by 1 
start with 900000 
maxvalue 999999999 
cache 200;
### 修改当前值  
1. 删除队列，然后新建相同队列，且开始于我们需要修改的值。
2. 修改增量，然后获取下一个值，然后将增量改回到原值。  
通过修改增量的方法:
-- 先计算当前队列值与目标值之间的差距， 获取并替换下方 increaseNumber
alter sequence sequenceName increment by increaseNumber nocache;
select sequenceName.nextval from dual;
alter sequence sequenceName increment by 1 nocache; 
通过重新建立队列的方法：
drop sequence sequenceName;
CREATE SEQUENCE  sequenceName  MINVALUE minNumber MAXVALUE maxNumber INCREMENT BY 1 START WITH currNumber NOCACHE  NOORDER  NOCYCLE;
