import click


# Provides new CLI flow subcmds
@click.group()
def cli():
    pass


@cli.group(help="Commands related to Flyte.")
def flyte():
    pass


@flyte.command(help="Register flow as a Flyte workflow.")
def register():
    click.echo("flyte register")
