import click
Commands can be attached to other commands of type Group.
This allows arbitrary nesting of scripts.
As an example here is a script that implements two commands for managing databases
As you can see, the group() decorator works like the command() decorator, but creates a Group
object instead which can be given multiple subcommands that can be attached with Group.add_command().
正如你所见，修饰符 group() 的用法与修饰符 command()一样， 只不过它创建的 Group 对象可以通过 Group.add_command()
将多个子命令关联到一起
@click.group()
def cli():
# 将 @click.command() 变为 @cli.command(), 相当于执行了下面的绑定操作：cli.add_command(initdb)
@cli.command()
def initdb():
    click.echo('Initialized the database')
@cli.command()
def dropdb():
    click.echo('Dropped the database')
# Instead of using the @group.command() decorator, commands can be decorated with the plain @click.command() decorator and  registered
# with a group later with group.add_command(). This could be used to split commands into multiple Python modules.
# 各子命令可以不使用修饰符@group.command(),而是通过@click.command()进行修饰然后通过group.add_command()命令注册到Group对象中。这样就可以被不同的python模块所使用。
# cli.add_command(initdb)
# cli.add_command(dropdb)
if __name__ == '__main__':
    cli()
D:\workplace\pythonPrograms\tutorials\learning_click>nestingCommands.py
Usage: nestingCommands.py [OPTIONS] COMMAND [ARGS]...
  --help  Show this message and exit.
Commands:
D:\workplace\pythonPrograms\tutorials\learning_click>nestingCommands.py initdb
Initialized the database
