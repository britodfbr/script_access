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
def infosaj0(ctx):
    ctx.obj = {}


@click.command()
@click.argument('filename')
def model0(filename):
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
def generator0(fileconfig, fileoutput):
    """Generate informativo SAJ."""
    click.echo(f'{fileconfig}, {fileoutput}')

infosaj0.add_command(model0, 'gen')
infosaj0.add_command(generator0)


@click.group()
@click.pass_context
def infosaj(ctx):
    """Generate informativo SAJ."""
    ctx.obj = {}
    
@infosaj.command()
@click.argument('subcommand')
@click.pass_context
def help(ctx, subcommand):
    """Show the help for specific command."""
    subcommand_obj = infosaj.get_command(ctx, subcommand)
    if subcommand_obj is None:
        click.echo("I don't know that command.")
    else:
        click.echo(subcommand_obj.get_help(ctx))

@click.command()
@click.option('-c',
              "--fileconfig",
              prompt="Your file config name",
              help="Provide your file YAML config name")
@click.option('-o',
              "--fileoutput",
              prompt="Your file output name",
              help="Provide your file HTML output name")
@click.pass_context
def generator(ctx, fileconfig, fileoutput):
    """Generate informativo SAJ."""
    click.echo(f'{fileconfig}, {fileoutput}')

    
@click.command()
@click.argument('fileconfig')
@click.pass_context
def model(ctx, fileconfig):
    """Generate model config file."""
    click.echo(f'{ctx.obj} {fileconfig}')

infosaj.add_command(model)
infosaj.add_command(generator)


if __name__ == '__main__':
    gen_model_conf()
