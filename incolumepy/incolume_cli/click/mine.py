import click
from incolumepy.others.xpto import gen_model_conf

@click.group()
@click.pass_context
@click.option('-f', "--fileconf", prompt="Your file config name", help="Provide your file config name")
def infosaj():
    pass

    
@click.pass_context
@infosaj.command(name='model')
def gen_model(fileconf=None):
    gen_model_conf(fileconf)

if __name__ == '__main__':
    gen_model_conf()