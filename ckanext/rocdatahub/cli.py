import click


@click.group(short_help="rocdatahub CLI.")
def rocdatahub():
    """rocdatahub CLI.
    """
    pass


@rocdatahub.command()
@click.argument("name", default="rocdatahub")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [rocdatahub]
