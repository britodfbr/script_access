import click
from incolumepy.others.xpto import gen_model_conf
import inspect
from pathlib import Path


@click.command()
@click.option('-m',
              '--model',
              is_flag=True,
              default=False,
              help='if need generate file configurate')
def test(model):
    if model:
        click.secho('Show', fg='green')
    else:
        click.secho('Show')


# @click.command()
# @click.option('-m',
#               '--model',
#               is_flag=False,
#               help='if need generate file configurate')
# @click.option('-c',
#               "--conffile",
#               prompt="Your file config name",
#               help="Provide your file config name")
# @click.option('-f',
#               "--filename",
#               prompt="Your file output name",
#               help="Provide your file output name")
# def infosaj(conffile, filename, model):
#     click.secho(f'{inspect.stack()[0][3]}', fg='red')
#     if model:
#         gen_model_conf(conffile)
#     click.secho(Path(filename).as_posix())


@click.group()
@click.pass_context
def infosaj(ctx):
    ctx.obj = {}


@click.command()
@click.argument('filename')
def model(filename):
    """Generate model config file."""
    click.echo(filename)


@click.command()
@click.option('-c',
              "--fileconfig",
              prompt="Your file config name",
              help="Provide your file config name")
@click.option('-o',
              "--fileoutput",
              prompt="Your file output name",
              help="Provide your file output name")
def generator(fileconfig, fileoutput):
    """Generate informativo SAJ."""
    click.echo(f'{fileconfig}, {fileoutput}')

infosaj.add_command(model, 'gen')
infosaj.add_command(generator)

if __name__ == '__main__':
    gen_model_conf()
