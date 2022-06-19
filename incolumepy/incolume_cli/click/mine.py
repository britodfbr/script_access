import click
from incolumepy.others.xpto import gen_model_conf
import inspect
from pathlib import Path


click.command()
def test():
    click.secho('Show', fg='green')
    

click.command()
@click.option(
    '-m', 
    '--model', 
    is_flag=False, 
    help='if need generate file configurate')
@click.option(
    '-c',
    "--conffile",
    prompt="Your file config name",
    help="Provide your file config name")
@click.option(
    '-f',
    "--filename",
    prompt="Your file output name",
    help="Provide your file output name")
def infosaj(conffile, filename, model):
    click.secho(f'{inspect.stack()[0][3]}', fg='red')
    if model:
        gen_model_conf(conffile)
    click.secho(Path(filename).as_posix())



if __name__ == '__main__':
    gen_model_conf()
