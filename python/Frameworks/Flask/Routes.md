``` Python
import flask
from flask import request
app = flask.Flask(__name__)
# flask route params  
这里的参数指的是url的path部分。  
``` Python
@app.route('/product/<name>')
def get_product(name):
  return "The product is " + str(name)
我们可以同时匹配多个参数， 并且赋予默认值。  
``` Python  
@app.route('/create/<first_name>/<last_name>')
def create(first_name=None, last_name=None):  
  return 'Hello ' + first_name + ',' +last_name  
而针对查询参数我们通过```request```获取, 假如我们现在会接收到这么一个请求: /hcos/rest?relation=332198, 那么我们如下配置即可
``` Python
@app.route('/hcos/rest')  
def hcop() -> json:
  relation = request.values.get('relation')
请求地址URL: ```http://host:port/hcos/rest?relation=332198```  
这样，请求可以被路由至此，并且可以获取到查询参数```relation```的值 **332198**.
