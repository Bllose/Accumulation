# JSONObject 打印参数
### 当存在不要触碰的字段时
SimplePropertyPreFilter filter = new SimplePropertyPreFilter();
filter.getExcludes().add("appName");
filter.getExcludes().add("scope");
JSONObject.toJSONString(executeList, filter);
