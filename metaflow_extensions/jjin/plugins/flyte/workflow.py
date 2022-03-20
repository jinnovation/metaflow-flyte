from typing import Callable, Optional

from flytekit import Workflow
from metaflow import current
from metaflow.graph import FlowGraph

# TODO: Package the code and submit to Flyte
# TODO: func to turn metaflow.DAGNode into flyte.PythonTask


class WorkflowConstructor:
    def __init__(self, echo: Callable = print):
        self.echo: Callable = echo

    @classmethod
    def from_metaflow_cli_obj(cls, obj) -> "WorkflowConstructor":
        return cls(echo=obj.echo)

    def build(self, flow_graph: FlowGraph) -> Workflow:
        self.echo(str(flow_graph))

        # Provided by @project decorator if present
        #
        # TODO: Require this?
        project: Optional[str] = current.get("project_name")
        domain: Optional[str] = current.get("branch_name")

        wf = Workflow(
            name=flow_graph.name,
        )

        self.echo("Ignoring all nodes in the workflow; stuff's WIP okay?")
        self.echo(f"Constructed shell Flyte workflow: {wf}")

        # TODO: package the workflow using the pyflyte cli bundled with Flytekit and upload it to the Flyte
        # backend.
        return wf
