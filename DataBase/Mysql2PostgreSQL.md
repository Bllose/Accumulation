# COMMENT  
不能像Mysql一样跟在字段后面， 而是单独使用 ```COMMENT```命令。  
**MYSQL**  
create table ASC_API_LOG_T
    log_business_id DECIMAL COMMENT '日志记录表主键',
    interface_name  VARCHAR(1000) COMMENT '接口名称',
    business_name   VARCHAR(1000) COMMENT '业务属性名称',
    business_type   VARCHAR(10) COMMENT '10：订单提交 20：订单取消 30：退库指令 40：创建SR   50:推送数据到CSPM',
    begin_date      VARCHAR(20) COMMENT '执行开始时间',
    end_date        VARCHAR(20) COMMENT '执行结束时间',
    url             VARCHAR(1000) COMMENT '请求URL',
    request_data    TEXT COMMENT '请求参数',
    response_data   TEXT COMMENT '返回参数',
    create_time     DATETIME COMMENT '创建时间',
    attr1           VARCHAR(1000) COMMENT '备用字段一',
    attr2           VARCHAR(1000) COMMENT '备用字段二',
    attr3           VARCHAR(1000) COMMENT '备用字段三',
    enable_flag     VARCHAR(10) COMMENT ' 有效性标识',
    err_message     TEXT COMMENT '错误信息记录'
**PostgreSQL**  
create table ASC_API_LOG_T
    log_business_id DECIMAL ,
    interface_name  VARCHAR(1000) ,
    business_name   VARCHAR(1000) ,
    business_type   VARCHAR(10) ,
    begin_date      VARCHAR(20) ,
    end_date        VARCHAR(20) ,
    url             VARCHAR(1000) ,
    request_data    TEXT ,
    response_data   TEXT ,
    create_time     timestamptz ,
    attr1           VARCHAR(1000) ,
    attr2           VARCHAR(1000) ,
    attr3           VARCHAR(1000) ,
    enable_flag     VARCHAR(10) ,
    err_message     TEXT
COMMENT ON COLUMN ASC_API_LOG_T.log_business_id is '日志记录表主键';
# 时间类型   
**MYSQL** _DATETIME_  
**PostgreSQL** _timestamp\[tz]_  
      typename,
      typlen
      pg_type
      typename ~ '^timestamp';
**MYSQL**  
`runoob_id` INT UNSIGNED AUTO_INCREMENT
**PostgreSQL**  
id serial NOT NULL
| 伪类型 | 储存大小 | 范围 |  
| --- | --- | --- |  
| SMALLSERIAL | 2字节 | 1 到 32,767 |  
| SERIAL | 4字节 | 1 到 2,147,483,647 |  
| BIGSERIAL | 8字节 | 1 到 922,337,2036,854,775,807 |  
MYSQL 需要通过 FUNCTION + 表的形式自行实现
PG 支持直接重新设定序列的当前起始值  
alter sequence sequence_name restart number;
create sequence sequence_name start number;
PG 中```update```和 ```delete```表不能使用别名, 会被识别为表名而报错。 
update table_name t 
set t.a = 'b'
where t.c = 'd'
ORACLE, MYSQL 都是可以正常运行的， 只有PG会报错。  
	count(1)
	Example_supplier_t t
	t.last_update_time desc;
如果在PG上执行如上SQL， 则会报如下错误:
SQL 错误 [42803]: ERROR: column "t.last_update_time" must appear in the GROUP BY clause or be used in an aggregate function
  ERROR: column "t.last_update_time" must appear in the GROUP BY clause or be used in an aggregate function
  ERROR: column "t.last_update_time" must appear in the GROUP BY clause or be used in an aggregate function
即，在```order by```中出现的字段，也需要出现在```group by```中或者在一个聚合方法(```sum,avg,count,min,max```)中使用。  
就如上例子， 需要适配PG，则需要修改为：  
	count(1)
	Example_supplier_t t
group by 
	t.last_update_time
	t.last_update_time desc;
