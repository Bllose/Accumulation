pip install PyQt5
pip install PyQt5-tools
# 使用Qt Designer  
安装了 PyQt5-tools 之后， 可以在```%PYTHON_HOME%\Lib\site-packages\qt5_applications\Qt\bin\designer.exe```找到Qt Designer    
制作好页面后保存为```.ui```文件。  
# 嵌入Python项目  
**通过```pyuic5```将```.ui```转化为```.py```**  
pyuic5 -o firstMainWin.py MyFirstMainWindow.ui
最后创建py入口，最终接入python项目:  
``` Python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from firstMainWin import *
class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
