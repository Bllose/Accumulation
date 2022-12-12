-- 以schema为维度查询表和表描述信息
	distinct tableName,
	tableComment
		relname as tableName,
		cast(obj_description(relfilenode, 'pg_class') as varchar) as tableComment
		pg_class a
		relname in (
			tablename
			pg_tables
			schemaname = 'ExampleExample' )) final
	final.tableComment is not null
	and final.tableComment != ''
	tableName,
	tableComment; 
-- 以表id为维度，获取列信息   
select oid from pg_class c where relname = 'Example_base_store_config_t';
-- 针对当前表Id获取列信息
select 	a.attname as "列名",
		concat_ws('', t.typname, substring(format_type(a.atttypid, a.atttypmod) from '\(.*\)')) as "字段类型",
		d.description as "备注"
from pg_attribute a, pg_type t, pg_description d
where a.attnum > 0
and a.attrelid = 16973
and a.atttypid = t."oid"
and d.objoid = a.attrelid
and d.objsubid = a.attnum;
-- 查询表下字段的备注信息
	distinct col.table_name,
	col.column_name,
	col.ordinal_position as o,
	d.description
	information_schema.columns col
join pg_class c on
	c.relname = col.table_name
left join pg_description d on
	d.objoid = c.oid
	and d.objsubid = col.ordinal_position
	col.table_schema = 'ExampleExample'
	and col.table_name = 'Example_return_apply_detail_t'
-- 通过查询到的备注信息， 生成创建字段备注命令
with original as(
	distinct col.table_name,
	col.column_name,
	col.ordinal_position as o,
	d.description
	information_schema.columns col
join pg_class c on
	c.relname = col.table_name
left join pg_description d on
	d.objoid = c.oid
	and d.objsubid = col.ordinal_position
	col.table_schema = 'ExampleExample'
	and col.table_name = 'Example_return_apply_detail_t'
group by col.table_name,
	col.column_name,
	col.ordinal_position,
	d.description
order by col.ordinal_position
select 'comment on column ' || table_name || '.' || column_name || ' is ''' ||  description || ''';' from original;
-- 查询表备注信息， 并生成添加表备注语句
with original_table as (			
	distinct final.tabname as table_name,
	final.comment as description,
	final.schemaname
		p.schemaname,
		c.relname as tabname,
		cast(obj_description(c.relfilenode, 'pg_class') as varchar) as comment
		pg_class c left join pg_tables p on c.relname = p.tablename
		p.schemaname = 'ExampleExample'
		and tablename = 'Example_api_log_t' ) final
	final.comment is not null
	final.tabname,
	final.comment,
	final.schemaname)
select 'comment on table ' || schemaname || '.' || table_name || ' is ''' || description || ''';' from original_table;
