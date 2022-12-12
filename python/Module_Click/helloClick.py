import click
@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(count, name):
    for x in range(count):
        click.echo(f"hello {name}!")
if __name__ == '__main__':
    hello()
click以及其优雅的方式简化了命令行调用时的参数接收逻辑，
并且兼顾了 help 文档的输出。
>helloClick.py --count=3
Your name: Bllose
hello Bllose!
hello Bllose!
hello Bllose!
>helloClick.py --help
Usage: helloClick.py [OPTIONS]
  --count INTEGER  Number of greetings.
  --name TEXT      The person to greet.
  --help           Show this message and exit.
