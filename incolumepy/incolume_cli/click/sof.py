import click


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}

    
@cli.command()
@click.argument('subcommand')
@click.pass_context
def help(ctx, subcommand):
    subcommand_obj = cli.get_command(ctx, subcommand)
    if subcommand_obj is None:
        click.echo("I don't know that command.")
    else:
        click.echo(subcommand_obj.get_help(ctx))