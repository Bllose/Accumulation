## 通用SQL部分 \<include refid="sql_name"/\>
当尝试使用通用SQL时，入参的名称可以通过名称获取，亦可以通过参数所属位置获取。  
- 通过位置获取  
```#{0.column_name, jdbcType=TYPE}```  
- 通过名称获取  
returnType functionName(@Param("param") paramTarget, ...);
```#{param.column_name, jdbcType=TYPE}```
> **为什么要使用位置获取参数？这即不安全，也没有特别方便。所有使用该SQL模块的方法， 都需要小心翼翼地对上参数位置， 这并不比添加名称容易。**
# IF ELSE
**Mybatis中没有 if ... else 的用法**  
通过\<choose/> \<when/> \<otherwish/> 实现。  
``` Mybatis
    <when test = "">
    </when>
    <otherwise>
    </otherwise>
</choose>
