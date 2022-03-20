import click
from metaflow import current


# Provides new CLI flow subcmds
@click.group()
def cli():
    pass


@cli.group(help="Commands related to Flyte.")
def flyte():
    pass


@flyte.command(help="Register flow as a Flyte workflow.")
@click.pass_context
def register(ctx):
    ctx.obj.echo(f"Project name: {current.project_name}")
    ctx.obj.echo(f"Branch name: {current.branch_name}")
