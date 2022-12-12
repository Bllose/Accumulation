# 信号/槽 机制  
``` python
self.closeWinBtn.clicked.connect(Widget.close)  
从如上代码可以理解信号、槽机制，编码结构如下：  
组件. 行为-信号 .connect(组件.行为-槽)   
官方描述: ```QObject.signal.connect(QObject.slot)```
  这与 callback 有什么本质区别？
