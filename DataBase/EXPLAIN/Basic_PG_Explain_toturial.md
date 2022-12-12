``` EXPLAIN [ ( option [, ...] ) ] sql_statement,```  
![语法](https://img-blog.csdnimg.cn/img_convert/28860657b59a990671bf412c7a345cd9.png)
explain (analyze true, buffers true)
select * from table_name;
| QUERY PLAN |
| Seq Scan on Example_api_log_t  (cost=0.00..10.20 rows=20 width=3400) (actual time=0.002..0.003 rows=0 loops=1) |
| Planning Time: 0.155 ms |
| Execution Time: 0.020 ms |
explain (analyze true, format JSON)
select * from Example_api_log_t;
| QUERY PLAN |
| \[<br> \{<br>    "Plan": {<br>      "Node Type": "Seq Scan",<br>      "Parallel Aware": false,<br>      "Relation Name": "Example_api_log_t",<br>      "Alias": "Example_api_log_t",<br>      "Startup Cost": 0.00,<br>      "Total Cost": 10.20,<br>      "Plan Rows": 20,<br>      "Plan Width": 3400,<br>      "Actual Startup Time": 0.003,<br>      "Actual Total Time": 0.003,<br>      "Actual Rows": 0,<br>      "Actual Loops": 1<br>    },<br>    "Planning Time": 0.051,<br>    "Triggers": [<br>    ],<br>    "Execution Time": 0.022<br>  }<br>] |
#### ANALYZE
这个选项会通过真实地执行SQL，从而获得真实情况下具体的执行时间和涉及的数据行数。由于这种机制，如果你还想在真实场景下分析```INSERT```, ```UPDATE```或者```DELETE```,但是又不想影响数据， 那么就需要在分析的SQL语句外包裹一层回退语句， 比如:
  EXPLAIN ANALYZE sql_statement;
ROLLBACK;
# EXPLAIN Basics  
The structure of a query plan is a tree of plan nodes. Nodes at the bottom level of the tree are scan nodes: they return raw rows from a table. There are different types of scan nodes for different table access methods: 
- sequential scans 
- index scans
- bitmap index scans
EXPLAIN SELECT * FROM tenk1;
                         QUERY PLAN
-------------------------------------------------------------
 Seq Scan on tenk1  (cost=0.00..458.00 rows=10000 width=244)
Seq Scan -> sequential scan plan  
Since this query has no _WHERE_ clause, it must scan all the rows of the table, so the planner has chosen to use a simple sequential scan plan. The numbers that are quoted in parentheses are (left to right):
- Estimated start-up cost. This is the time expended before the output phase can begin, e.g., time to do the sorting in a sort node.
- Estimated total cost. This is stated on the assumption that the plan node is run to completion, i.e., all available rows are retrieved. In practice a node's parent node might stop short of reading all available rows (see the _LIMIT_ example below).
- Estimated number of rows output by this plan node. Again, the node is assumed to be run to completion.
- Estimated average width of rows output by this plan node (in bytes).
