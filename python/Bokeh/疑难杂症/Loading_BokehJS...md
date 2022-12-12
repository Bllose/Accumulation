[Bokeh plot not showing in Jupyter. Only says "Loading BokehJS ..."](https://stackoverflow.com/questions/41841261/bokeh-plot-not-showing-in-jupyter-only-says-loading-bokehjs)  
Bokeh plots rely on a JavaScript library, BokehJS. By default (and by popular demand) BokehJS is loaded remotely from a CDN (specifically, from https://cdn.bokeh.org). 
Accordingly, viewing a Bokeh plot that is configured to use CDN resource requires an active and working network connection.
But it's possible to use "inline" resources, which means the BokehJS library is included directly in the HTML output that Bokeh (the python library) generates. 
The easiest way to to do this is to set the environment variable:
```BOKEH_RESOURCES=inline```  
before you run your script or the notebook server. There are other ways to specify resources, though, too. For more details see the documentation.  
另一种解决方法:  
``` Python
from bokeh.resources import INLINE
import bokeh.io
bokeh.io.output_notebook(INLINE)
