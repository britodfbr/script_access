import click
from operator import mul
from functools import reduce

@click.command()
@click.argument('vals', type=int, nargs=-1)
def process(vals):
    print(vals)
    print(f'The sum is {sum(vals)}')
    print(f'The product is {reduce(mul, vals, 1)}')


@click.command()
@click.option('-s', '--string', default='guest')
def output(string: str):
    click.echo(string)


@click.command()
@click.option('-n', "--name", prompt="Your name", help="Provide your name")
def hello(name):
    click.echo(f"Hello, {name}")


@click.command()
def coloured():
    click.secho('Hello there', fg="red", bold=True)
    

@click.command()
@click.option('--green', is_flag=True, help='message in blue color')
def flag(green):

    if green:
        click.secho('Hello there', fg='green')
    else:
        click.secho('Hello there')


if __name__ == '__main__':
    process()