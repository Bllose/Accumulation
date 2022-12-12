 |-- greetings/
 |-- hello/
 # 创建一个可被引用的模块
mkdir greetings
cd greetings
** 初始化 **
$ go mod init example.com/greetings
go: creating new go.mod: module example.com/greetings
创建文件```greetings.go```
package greetings
import "fmt"
// Hello returns a greeting for the named person.
func Hello(name string) string {
    // Return a greeting that embeds the name in a message.
    message := fmt.Sprintf("Hi, %v. Welcome!", name)
    return message
This function takes a _name_ **parameter** whose type is _string_. The function also returns a _string_. 
In Go, a function whose name starts with a **capital** letter can be called by a function not in the same package.
This is known in Go as an **exported name**.
![example](https://golang.org/doc/tutorial/images/function-syntax.png)  
# 创建一个引用自定义模块的方法
mkdir hello
$ go mod init example.com/hello
go: creating new go.mod: module example.com/hello
package main
    "fmt"
    "example.com/greetings"
func main() {
    // Get a greeting message and print it.
    message := greetings.Hello("Gladys")
    fmt.Println(message)
平时情况下，我们需要将之前的模块发布到对应仓库，才能被现在的方法找到并下载。 现在由于我们并没有真正发布，我们需要重定向一下```example.com/greetings```, 从而让go项目可以找到它。
$ go mod edit -replace example.com/greetings=../greeting
这时候打开```go.mod```可以看到如下内容：  
module example.com/hello
replace example.com/greetings => ../greeting
然后我们通过```tidy```命令，同步还未跟踪上的依赖模块。
$ go mod tidy
go: found example.com/greetings in example.com/greetings v0.0.0-00010101000000-000000000000
这时候打开```go.mod```可以看到如下内容:
module example.com/hello
replace example.com/greetings => ../greetings
require example.com/greetings v0.0.0-00010101000000-000000000000
最后，执行hello
$ go run .
Hi, Gladys. Welcome!
