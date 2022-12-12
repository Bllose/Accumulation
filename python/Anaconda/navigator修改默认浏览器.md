1. 打开 anaconda prompt
2. 输入 ``` jupyter notebook --generate-config```  
(base) C:\Users\Administrator>jupyter notebook --generate-config
Writing default config to: C:\Users\Administrator\.jupyter\jupyter_notebook_config.py
3. 打开如上配置文件， 添加配置
import webbrowser
webbrowser.register("chrome",None,webbrowser.GenericBrowser(u"C:\\ProgramFiles(x86)\\Google\\Chrome\\Application\\chrome.exe"))
c.NotebookApp.browser = 'chrome'
