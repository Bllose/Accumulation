mkdir hello
# 交由GO进行管理（依赖跟踪）
go mod init example/hello
go: creating new go.mod: module example/hello
vi hello.go
# 寻找其他可用包
访问 pkg.go.dev ，查找包，例如： "quote"。 从而知道该包属于 ```rsc.io/quote```模块
从而我们可以导入我们项目```import "rsc.io/quote"```, 然后使用它```fmt.Println(quote.Go())```。
** 添加对新模块得依赖，并生成sum文件 **  
go mod tidy
go: finding module for package rsc.io/quote
go: downloading rsc.io/quote v1.5.3-pre1
go: downloading rsc.io/quote v1.5.2
go: found rsc.io/quote in rsc.io/quote v1.5.2
go: downloading rsc.io/sampler v1.3.0
go: downloading golang.org/x/text v0.0.0-20170915032832-14c0d48ead0c
cat go.sum
golang.org/x/text v0.0.0-20170915032832-14c0d48ead0c h1:qgOY6WgZOaTkIIMiVjBQcw93ERBE4m30iBm00nkL0i8=
golang.org/x/text v0.0.0-20170915032832-14c0d48ead0c/go.mod h1:NqM8EUOU14njkJ3fqMW+pc6Ldnwhi/IjpwHt7yyuwOQ=
rsc.io/quote v1.5.2 h1:w5fcysjrx7yqtD/aO+QwRjYZOKnaM9Uh2b40tElTs3Y=
rsc.io/quote v1.5.2/go.mod h1:LzX7hefJvL54yjefDEDHNONDjII0t9xZLPXsUe+TKr0=
rsc.io/sampler v1.3.0 h1:7uVkIFmeBqHfdjD+gZwtXXI+RODJ2Wc4O7MPEh/QiW4=
rsc.io/sampler v1.3.0/go.mod h1:T1hPZKmBbMNahiBKFy5HrXp6adAjACjK9JXDnKaTXpA=
