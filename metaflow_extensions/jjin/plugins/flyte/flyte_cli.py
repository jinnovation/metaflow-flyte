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
        default_domain="staging",
        # image_config=get_image_config(img_name="myapp:v1"),
        image_config=get_image_config(img_name="mfext:v1"),
    )

    # TODO: Create the project if not present??
    #
    # obj.flyte_cluster.client.register_project

    obj.workflow_constructor = WorkflowConstructor.from_metaflow_cli_obj(obj)
    wf, tasks = obj.workflow_constructor.build(obj.graph)
    obj.workflow = wf
    obj.tasks = tasks


@flyte.command(help="Register flow as a Flyte workflow.")
@click.pass_obj
def register(obj):
    obj.echo(f"Project name: {current.project_name}")
    obj.echo(f"Branch name: {current.branch_name}")
    for task in obj.tasks:
        obj.flyte_cluster.register(task)
    obj.flyte_cluster.register(obj.workflow)
    obj.echo("Registered Flyte workflow")

    launch_plan: LaunchPlan = LaunchPlan.get_or_create(obj.workflow)
    obj.flyte_cluster.register(launch_plan)
