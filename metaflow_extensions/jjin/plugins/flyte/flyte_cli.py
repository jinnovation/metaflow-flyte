import click
from metaflow import current

from metaflow_extensions.jjin.plugins.flyte.workflow import WorkflowConstructor


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


@flyte.command(help="Compile to Flyte workflow.")
@click.pass_obj
def compile(obj):
    ctor = WorkflowConstructor.from_metaflow_cli_obj(obj)

    obj.echo(f"Project name: {current.project_name}")
    obj.echo(f"Branch name: {current.branch_name}")
    wf = ctor.build(obj.graph)
