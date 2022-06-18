import click
from incolumepy.others.xpto import gen_model_conf

@click.group()
@click.pass_context
def infosaj():
    pass


@click.command()
@click.option('-f', "--fileconf", prompt="Your file config name", help="Provide your file config name")
def gen_model(fileconf):
    gen_model_conf(fileconf)


infosaj.add_command(gen_model, 'genmodel')


if __name__ == '__main__':
    gen_model_conf()