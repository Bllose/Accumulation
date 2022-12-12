import click
# 通过@click.option() 添加的为可选参数
# 通过@click.argument() 添加的为必输参数
@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo(f"Hello {name}!")
In the code you wrote so far there is a block at the end of the file which looks like this:
if __name__ == '__main__': .
This is tranditionally how a standalone Python file looks like. With Click you can continue 
doing that, but there are better ways through setuptools.
到目前为止，你写的代码块尾部，都有一段像 if __name__ == '__main__': 这样的一段代码。
这是python独立文件的传统写法。使用click模块时，依然可以如此写，但是通过setuptools模块，有更好的实现方式。
There are two main (and many more) reasons for this:
这里有两个主要的使用原因。
The first one is that setuptools automatically generates executable wrappers for Windows so your
command line utilities work on Windows too.
其一，在Windows下，setuptools会自动创建一个可执行的包裹程序，从而使得你的命令行（command line utilities）？也能在Windows下执行。
The second reason is that setuptools scripts work with virtualenv on Unix without the virtualenv
having to be activated. This is a very useful concept which allows you to bundle your scripts
with all requirements into a virtualenv.  
其二是在Unix下，setuptools在没有激活的virtualenv下依然可以与virtualenv很好地协同工作。这是一个很有用的概念，允许你将所有依赖的包
一起绑定进入virtualenv.
if __name__ == '__main__':
    hello()
D:\workplace\pythonPrograms\tutorials\learning_click>addingParameters.py
Usage: addingParameters.py [OPTIONS] NAME
Try 'addingParameters.py --help' for help.
Error: Missing argument 'NAME'.
D:\workplace\pythonPrograms\tutorials\learning_click>addingParameters.py --help
Usage: addingParameters.py [OPTIONS] NAME
  --count INTEGER  number of greetings
  --help           Show this message and exit.
D:\workplace\pythonPrograms\tutorials\learning_click>addingParameters.py Bllose
Hello Bllose!
D:\workplace\pythonPrograms\tutorials\learning_click>addingParameters.py --count=3 Bllose
Hello Bllose!
Hello Bllose!
Hello Bllose!
