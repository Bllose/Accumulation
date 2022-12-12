# 当cdn.bokeh.org被墙时  
```bokeh.resource```  
``` Python
def _cdn_base_url() -> str:
    return "https://cdn.bokeh.org"
修改为 将该地址修改为自己可以识别的地址进行获取
