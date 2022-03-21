from typing import Optional

import click
from flytekit import LaunchPlan
from flytekit.core.context_manager import get_image_config
from flytekit.remote.remote import FlyteRemote
from metaflow import current
from metaflow.exception import (FlyteMissingProjectAndBranchException,
                                FlyteNotReadyException)

from metaflow_extensions.jjin.plugins.flyte.workflow import WorkflowConstructor


# Provides new CLI flow subcmds
@click.group()
def cli():
    pass


@cli.group(help="Commands related to Flyte.")
@click.pass_obj
def flyte(obj):
    # TODO: Initialize flytekit.remote.remote.FlyteRemote; set to obj.flyte_cluster
    #
    # https://docs.flyte.org/projects/flytekit/en/latest/generated/flytekit.remote.remote.FlyteRemote.html

    project_name: Optional[str] = current.get("project_name")
    branch_name: Optional[str] = current.get("branch_name")

    if not project_name or not branch_name:
        raise FlyteMissingProjectAndBranchException

    obj.flyte_cluster = FlyteRemote(
        "localhost:30081",
        insecure=True,
        default_project=project_name,
        default_domain=branch_name,
        image_config=get_image_config(img_name="myapp:v1"),
    )

    # TODO: Create the project if not present??
    #
    # obj.flyte_cluster.client.register_project

    obj.workflow_constructor = WorkflowConstructor.from_metaflow_cli_obj(obj)
    obj.workflow = obj.workflow_constructor.build(obj.graph)


@flyte.command(help="Register flow as a Flyte workflow.")
@click.pass_obj
def register(obj):
    obj.echo(f"Project name: {current.project_name}")
    obj.echo(f"Branch name: {current.branch_name}")
    obj.flyte_cluster.register(obj.workflow)


@flyte.command(help="Compile to Flyte workflow.")
@click.pass_obj
def compile(obj):
    obj.echo(f"Project name: {current.project_name}")
    obj.echo(f"Branch name: {current.branch_name}")
    wf = obj.workflow
    obj.echo(f"Ready? {wf.ready()}")

    if not wf.ready():
        raise FlyteNotReadyException

    launch_plan: LaunchPlan = LaunchPlan.get_or_create(wf)

    # https://docs.flyte.org/projects/flytekit/en/latest/generated/flytekit.remote.remote.FlyteRemote.html
    # obj.flyte_cluster.execute(
    #     launch_plan,
    #     project=current.project_name,
    #     domain=current.branch_name,
    # )
