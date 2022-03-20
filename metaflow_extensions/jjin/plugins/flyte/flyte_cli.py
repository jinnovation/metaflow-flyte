import click
from metaflow import current

from metaflow_extensions.jjin.plugins.flyte.workflow import WorkflowConstructor
from flytekit import LaunchPlan


# Provides new CLI flow subcmds
@click.group()
def cli():
    pass


@cli.group(help="Commands related to Flyte.")
def flyte():
    # TODO: Initialize flytekit.remote.remote.FlyteRemote; set to obj.flyte_cluster
    #
    # https://docs.flyte.org/projects/flytekit/en/latest/generated/flytekit.remote.remote.FlyteRemote.html
    pass


@flyte.command(help="Register flow as a Flyte workflow.")
@click.pass_context
def register(ctx):
    ctx.obj.echo(f"Project name: {current.project_name}")
    ctx.obj.echo(f"Branch name: {current.branch_name}")


@flyte.command(help="Compile to Flyte workflow.")
@click.pass_obj
def compile(obj):
    print(obj.graph.nodes["start"])
    ctor = WorkflowConstructor.from_metaflow_cli_obj(obj)

    obj.echo(f"Project name: {current.project_name}")
    obj.echo(f"Branch name: {current.branch_name}")
    wf = ctor.build(obj.graph)

    obj.echo(f"Ready? {wf.ready()}")

    launch_plan: LaunchPlan = LaunchPlan.get_or_create(wf)

    # https://docs.flyte.org/projects/flytekit/en/latest/generated/flytekit.LaunchPlan.html
    # obj.flyte_cluster.execute(
    #     launch_plan,
    #     project=current.project_name,
    #     domain=current.domain_name,
    # )
