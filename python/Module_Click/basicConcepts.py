import click
# A function becomes a Click command line tool by decorating it through click.command().
# At its simplest, just decorating a function with this decorator will make it into a callable script.
# 通过给方法添加修饰语句 click.command()，可以将它变成一个Click的命令行工具。
# 最简单的使用方法，直接再方法上添加这个修饰语句，那么这个方法就变成一个可以被调用的脚本。
# What's happening is that the decorator converts the function into a Command which then can be invoked.
# 实际上，该修饰语句将该方法传入了 Command() 方法中，从而将它转化为可被调用的对象
@click.command()
def hello():
    click.echo('Hello World!')
if __name__ == '__main__':
    hello()
D:\workplace\pythonPrograms\tutorials\learning_click>basicConcepts.py
Hello World!
D:\workplace\pythonPrograms\tutorials\learning_click>basicConcepts.py --help
Usage: basicConcepts.py [OPTIONS]
  --help  Show this message and exit.
