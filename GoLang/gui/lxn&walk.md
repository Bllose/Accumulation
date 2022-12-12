go get github.com/akavel/rsrc
go get github.com/lxn/win
go get github.com/lxn/walk
# 官方入门教程  
首先创建两个文件  
test.exe.manifest
这两个文件放在同一个目录下即可  
#### test.go  
package main
	"github.com/lxn/walk"
	. "github.com/lxn/walk/declarative"
	"strings"
func main() {
	var inTE, outTE *walk.TextEdit
	MainWindow{
		Title:   "SCREAMO",
		MinSize: Size{600, 400},
		Layout:  VBox{},
		Children: []Widget{
			HSplitter{
				Children: []Widget{
					TextEdit{AssignTo: &inTE},
					TextEdit{AssignTo: &outTE, ReadOnly: true},
			PushButton{
				Text: "SCREAM",
				OnClicked: func() {
					outTE.SetText(strings.ToUpper(inTE.Text()))
#### test.manifest  
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
    <assemblyIdentity version="1.0.0.0" processorArchitecture="*" name="SomeFunkyNameHere" type="win32"/>
    <dependency>
        <dependentAssembly>
            <assemblyIdentity type="win32" name="Microsoft.Windows.Common-Controls" version="6.0.0.0" processorArchitecture="*" publicKeyToken="6595b64144ccf1df" language="*"/>
        </dependentAssembly>
    </dependency>
    <application xmlns="urn:schemas-microsoft-com:asm.v3">
        <windowsSettings>
            <dpiAwareness xmlns="http://schemas.microsoft.com/SMI/2016/WindowsSettings">PerMonitorV2, PerMonitor</dpiAwareness>
            <dpiAware xmlns="http://schemas.microsoft.com/SMI/2005/WindowsSettings">True</dpiAware>
        </windowsSettings>
    </application>
</assembly>
### 下面是执行与运行  
# mod 模式下  
go mod init exmple.com/test
go mod tidy
在这种情况下， 会出现一个对话框， 背后还会多出一个 ```cmd``` 窗口。
如果不想要多出来的 ```cmd``` 窗口，就在 ```build``` 时使用如下命令。  
go build -ldflags="-H windowsgui"  
### 另外补充  
在这种情况下， ```test.exe.manifest``` 文件得一直跟着 ```test.exe```文件， 否则无法运行。 如果想要摆脱这个束缚， 则需要使用工具 ```rsrc```。   
首先，先编译 ```rsrc``` 。然后执行命令 ```rsrc -manifest test.manifest -o rsrc.syso```。   
这时候目录下文件是这样的:  
test.manifest
rsrc.syso
在这种情况下执行 ```build```， 跑出来的 exe 文件就可以独立运行了
