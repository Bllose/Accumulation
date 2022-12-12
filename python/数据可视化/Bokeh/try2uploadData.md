``` Python
import pandas as pd
df = pd.read_csv(r'D:\datas\target_data.csv')
通过pandas直接加载一个数据文件，将其转化为数组对象。    
``` Python
df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 51 entries, 0 to 50
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype 
---  ------    --------------  ----- 
 0   months    51 non-null     object
 1   purchase  51 non-null     int64 
 2   apply     51 non-null     int64 
 3   finish    51 non-null     int64 
dtypes: int64(3), object(1)
memory usage: 1.7+ KB
可以看出，本质上是通过DataFrame类型，对数据进行承载。  其中第一个字段是一个时间对象， ```months``` 但是导入之后，类型为```object```， 这意味着，它不能直接当作一个时间来使用。  
``` Python  
df['months']=pd.to_datetime(df['months'], format='%Y-%m')
type(df['months'][0])
pandas._libs.tslibs.timestamps.Timestamp
通过```to_datetime```方法，将这个object对象列，类型转变为```Timestamp```.
``` Python
from bokeh.io import output_notebook, show
from bokeh.resources import INLINE
from bokeh.plotting import figure
output_notebook(INLINE)
```INLINE``` 的作用是告诉bokeh使用本地资源。 因为它默认会加载网络上的js脚本。 但是我本地不能联网，故使用本地资源进行编译、加载。  
相关QA：[Bokeh plot not showing in Jupyter. Only says "Loading BokehJS ..."](https://stackoverflow.com/questions/41841261/bokeh-plot-not-showing-in-jupyter-only-says-loading-bokehjs)  
``` Python
s1 = figure(width=1200, plot_height=500, x_axis_type="datetime", x_axis_label="time")
s1.circle('months', 'purchase', size=5, color="navy", alpha=0.5, source=df)
``` Python
s1 = figure(width=1200, plot_height=500, x_axis_type="datetime", x_axis_label="time")
# s1.line(df['months'], df['purchase'], legend="purchase", line_width=3, line_color='red')
s1.line(df['months'], df['apply'], legend="apply", line_width=3, line_color='blue')
s1.line(df['months'], df['finish'], legend="finish", line_width=3, line_color='green')
``` Python
colors = ['red', 'green', 'yellow', 'blue', 'navy', 'orange']
columns = [df_amount['purchase'], df_amount['apply'], df_amount['finish']]
labels = ['purchase', 'apply', 'finish']
s3 = figure(width=1200, plot_height=500, x_axis_type="datetime", x_axis_label="time")
for column, color, label in zip(columns, colors, labels):  
    s3.line(df_amount['months'], column, legend_label=label, line_width=3, line_color=color)
> ```zip()``` 函数将可迭代对象作为参数， 将对象中对应的元素打包成一个个元组， 然后返回由这些元组组成的列表。
