explain select
	ct.check_no,
	adt.device_id,
	ct.logistics_no,
	row_number() over( partition by adt.device_id
	ct.create_time desc ) rn
	ExampleExample.Example_check_t ct
inner join ExampleExample.Example_check_detail_t adt on
	adt.check_id = ct.check_id
	ct.check_type in ('7',
	and ct.enable_flag = 'Y'
	and ct.status != '2'
WindowAgg  (cost=179060.12..192133.10 rows=653649 width=56)                                                                                              |
  ->  Sort  (cost=179060.12..180694.24 rows=653649 width=48)                                                                                             |
        Sort Key: adt.device_id, ct.create_time DESC                                                                                                     |
        ->  Hash Join  (cost=26736.40..104146.40 rows=653649 width=48)                                                                                   |
              Hash Cond: (adt.check_id = ct.check_id)                                                                                                    |
              ->  Seq Scan on Example_check_detail_t adt  (cost=0.00..61289.46 rows=2555746 width=10)                                                        |
              ->  Hash  (cost=26018.08..26018.08 rows=57466 width=50)                                                                                    |
                    ->  Seq Scan on Example_check_t ct  (cost=0.00..26018.08 rows=57466 width=50)                                                            |
                          Filter: (((check_type)::text = ANY ('{7,11}'::text[])) AND ((status)::text <> '2'::text) AND ((enable_flag)::text = 'Y'::text))|
```Seq Scan```  
Notice that the _EXPLAIN_ output shows the _WHERE_ clause being applied as a “filter” condition attached to the **Seq Scan** plan node. This means that the plan node checks the condition for each row it scans, and outputs only the ones that pass the condition. The estimate of output rows has been reduced because of the _WHERE_ clause. However, the scan will still have to visit all 10000 rows, so the cost hasn't decreased; in fact it has gone up a bit (by 10000 * **cpu_operator_cost**, to be exact) to reflect the extra CPU time spent checking the _WHERE_ condition.
