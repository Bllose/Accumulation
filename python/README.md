# 创建虚拟环境  
**Windows**下安装虚拟环境  
C:\user>pip install virtualenv
Looking in indexes: http://mirrors.tools.Example.com/pypi/simple
Collecting virtualenv
  Downloading http://mirrors.tools.Example.com/pypi/packages/ac/8a/05e8d8a3ac88a3c4ebec1fe2b1b4730e6e6ebdddb52cfd6cea6803de4624/virtualenv-20.10.0-py2.py3-none-any.whl (5.6 MB)
     |████████████████████████████████| 5.6 MB 3.3 MB/s
Collecting platformdirs<3,>=2
  Downloading http://mirrors.tools.Example.com/pypi/packages/b1/78/dcfd84d3aabd46a9c77260fb47ea5d244806e4daef83aa6fe5d83adb182c/platformdirs-2.4.0-py3-none-any.whl (14 kB)
Collecting backports.entry-points-selectable>=1.0.4
  Downloading http://mirrors.tools.Example.com/pypi/packages/6d/2e/a6789183415658c7f2c41da8599d53077bd222233039f5c92bffbf23b28d/backports.entry_points_selectable-1.1.1-py2.py3-none-any.whl (6.2 kB)
Requirement already satisfied: six<2,>=1.9.0 in d:\etc\python\python39_64\lib\site-packages (from virtualenv) (1.15.0)
Collecting distlib<1,>=0.3.1
  Downloading http://mirrors.tools.Example.com/pypi/packages/28/36/4bdfb663826d6deedc30b179a7b7876a86943cec9fcfc3f1638489fd8b09/distlib-0.3.3-py2.py3-none-any.whl (496 kB)
     |████████████████████████████████| 496 kB 6.4 MB/s
Collecting filelock<4,>=3.2
  Downloading http://mirrors.tools.Example.com/pypi/packages/e8/3b/b59c7bcacc4cccafcd6e927a9e191268657e79a0a75530132cbf03b22c47/filelock-3.4.0-py3-none-any.whl (9.8 kB)
Installing collected packages: platformdirs, filelock, distlib, backports.entry-points-selectable, virtualenv
Successfully installed backports.entry-points-selectable-1.1.1 distlib-0.3.3 filelock-3.4.0 platformdirs-2.4.0 virtualenv-20.10.0
**新建工作目录，并创建虚拟环境**  
D:\workplace>mkdir pythonPrograms
D:\workplace>cd pythonPrograms
D:\workplace\pythonPrograms>ls
# 在当前目录下初始化虚拟环境
D:\workplace\pythonPrograms>virtualenv venv
created virtual environment CPython3.9.2.candidate.1-64 in 724ms
  creator CPython3Windows(dest=D:\workplace\pythonPrograms\venv, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\cwx921932\AppData\Local\pypa\virtualenv)
    added seed packages: pip==21.3.1, setuptools==58.3.0, wheel==0.37.0
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
# 激活刚才创建的虚拟环境
D:\workplace\pythonPrograms>venv\scripts\activate
# 退出当前虚拟环境
(venv) D:\workplace\pythonPrograms>deactivate
D:\workplace\pythonPrograms>
## [pip/setuptools/wheels](https://packaging.python.org/en/latest/tutorials/installing-packages/)
#### pip  
推荐使用```pip```进行安装。更多细节请查看[pip文档](https://pip.pypa.io/en/latest/),里面包含了完整的[指导手册](https://pip.pypa.io/en/latest/cli/)。  
#### setuptools  
## [pytest](https://www.pytest.org/)
Python项目开箱即用的测试模块
## [click](https://click.palletsprojects.com/)
Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as neccessary. It's the "Command Line Interface Creation Kit". It's highly configurable but comes with sensible defaults out of the box.
## [sqlalchemy](https://www.sqlalchemy.org/)
Python下的数据库工具
## pyinstaller  
### 针对 ModuleNotFoundError: No module named 'xxxxxx' 情形  
首先确认当前命令行环境下是否可以读取到该包  
``` pip list | grep xxxxxx ```  
如果在代码中隐性地引用了第三方包， 则在安装命令的参数中添加: ```--hidden-import=xxxxxx ```  
PS: ```pyinstaller --hidden-import=lxml -F mvncheck.py```  
假如你的代码中引用了还未安装的自己的模块， 则将自己模块添加到安装目录: ``` --path /your/moduel/path ```  
PS: ``` pyinstaller --path D:\etc\Python\Python39_64\Lib\bllools -F mvncheck.py ```
