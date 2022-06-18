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


@click.command()
@click.argument('word')
@click.option('--shout/--no-shout', default=False)
def zflag(word, shout):
    if shout:
        click.secho(word.upper(), fg='red')
    else:
        click.echo(word)
        

@click.command()
@click.option('--word', '-w', multiple=True)
def multiples(word):
    """ multiples entrances.
    
    ex: zmult -w a --word b -w c -w d
    """
    click.secho('\n'.join(word))


@click.command()
@click.argument('file_name', type=click.File('r'))
@click.argument('lines', default=-1, type=int)
def head(file_name, lines):

    counter = 0

    for line in file_name:

        print(line.strip())
        counter += 1

        if counter == lines: 
            break


# Group commands
@click.group()
def messages():
  pass


@click.command()
def generic():
    click.echo('Hello there')


@click.command()
def welcome():
    click.echo('Welcome')


messages.add_command(generic)
messages.add_command(welcome)
          

@click.group()
def cli():
  pass


@cli.command(name='gen')
def generic():
    click.echo('Hello there')


@cli.command(name='wel')
def welcome():
    click.echo('Welcome')


if __name__ == '__main__':
    process()