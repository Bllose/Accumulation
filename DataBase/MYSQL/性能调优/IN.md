结论：如果需要适应 IN 条件， 则 IN 语句中一定是固定值， 而不是一个子查询。 否则性能直线下降。
update Example_return_apply_detail_t t
set t.draft_status   = 'N',
    last_update_by   = 'N',
    last_update_time = now()
where t.device_id in (select cd.device_id from Example_check_detail_t cd where cd.check_id = 123);
| id | select\_type | table | partitions | type | possible\_keys | key | key\_len | ref | rows | filtered | Extra |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | UPDATE | t | NULL | index | NULL | PRIMARY | 8 | NULL | 1 | 100 | Using where |
| 2 | DEPENDENT SUBQUERY | cd | NULL | ref | ASC\_CHECK\_DETAIL\_N2,ASC\_CHECK\_DETAIL\_N1,ASC\_CHECK\_DETAIL\_N3 | ASC\_CHECK\_DETAIL\_N2 | 9 | const | 1 | 100 | Using where |  
这段SQL在真实的查询场景中非常的慢。 根本原因为 ```DEPENDENT SUBQUERY``` 的基本原理为依赖性查询。  
所谓的依赖性，在此处的意思为， 子查询```select cd.device_id from Example_check_detail_t cd where cd.check_id = 123```依赖于外层的【查询结果】。  
这里的查询结果指的是， MYSQL尝试确认并收集【可能需要更新】的信息（就当前语句而言，并没有其他过滤条件，所以是灾难性的全表扫描）。  
当拿到这些可能需要更新的信息后， 再一条一条通过子查询进行匹配， 这就是为什么子查询走了索引但是性能还是极差。  
``` SQL  
select count(1) from Example_return_apply_detail_t where draft_status != 'N' and last_update_by != 'N' and device_id is not null;
| count(1) |  
| --- |  
| 1431266 |  
update Example_return_apply_detail_t t
set t.draft_status   = 'N',
    last_update_by   = 'N',
    last_update_time = now()
where t.device_id in (select cd.device_id from Example_check_detail_t cd where cd.check_id = 123);
| id | select\_type | table | partitions | type | possible\_keys | key | key\_len | ref | rows | filtered | Extra |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | UPDATE | t | NULL | index | NULL | PRIMARY | 5 | NULL | 1419017 | 100 | Using where |
| 2 | DEPENDENT SUBQUERY | cd | NULL | ref | ASC\_CHECK\_DETAIL\_N2,ASC\_CHECK\_DETAIL\_N1,ASC\_CHECK\_DETAIL\_N3 | ASC\_CHECK\_DETAIL\_N2 | 6 | const | 1 | 10 | Using where |
update Example_return_apply_detail_t t
set t.draft_status   = 'N',
    last_update_by   = 'N',
    last_update_time = now()
where t.device_id in ('123', '456', '789');
| id | select\_type | table | partitions | type | possible\_keys | key | key\_len | ref | rows | filtered | Extra |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | UPDATE | t | NULL | range | PRIMARY | PRIMARY | 5 | const | 3 | 100 | Using where |
