import click
from incolumepy.others.xpto import gen_model_conf
import inspect

@click.group()
@click.pass_context
def infosaj():
    pass


@infosaj.command()
@click.option('-f',
              "--fileconf",
              prompt="Your file config name",
              help="Provide your file config name")
def gen_model(fileconf):
    click.secho(f'{inspect.stack()[0][3]}', fg='red')
    gen_model_conf(fileconf)


@infosaj.command()
@click.option('-f',
              "--fileconf",
              prompt="Your file config name",
              help="Provide your file config name")
def gen_infosaj(fileconf, fout):
    click.secho(f'{inspect.stack()[0][3]}', fg='red')
    gen_model_conf(fileconf)

infosaj.add_command(gen_model, 'genmodel')
infosaj.add_command(gen_infosaj, 'geninfo')


if __name__ == '__main__':
    gen_model_conf()
