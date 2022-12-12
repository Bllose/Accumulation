进入虚拟环境，使用```pip```安装必要包  
如果有依赖自己项目中其他模块， 则使用```--path```将自己项目也加入编译路径。  
如果有pyinstaller无法识别的模块引用，则使用```--hidden-import```指定资源模块。  
```pyinstaller --path D:\etc\Python\Python39_64\Lib\bllools --hidden-import bs4 -F finder.py```  
### ModuleNotFoundError: No module named 'xxx'  
首先， 先确认自己使用的 pyinstaller 属于哪个环境。   
类linux上有命令```whereis pyinstaller```  
windows上有待补充  
然后确认当前环境的 python 与 pyinstaller 是否属于同一个环境.  
```python --version``` ```whereis python```  
WINDOWS 下 ```echo %path%``` ```echo %PYTHON_HOME%``` ```echo %UnderDevTools%```    
当且仅当 pyinstaller 与当前运行 python 环境一致时， 才能最终解决顽固```ModuleNotFoundError```问题
