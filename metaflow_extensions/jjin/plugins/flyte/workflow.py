from typing import Callable, List, Optional, Tuple

from flytekit import PythonFunctionTask, Workflow, task
from metaflow import current
from metaflow.graph import FlowGraph

# TODO: Package the code and submit to Flyte
# TODO: func to turn metaflow.DAGNode into flyte.PythonTask


@task
def hello_world():
    print("hello world")


class WorkflowConstructor:
    def __init__(self, echo: Callable = print):
        self.echo: Callable = echo

    @classmethod
    def from_metaflow_cli_obj(cls, obj) -> "WorkflowConstructor":
        return cls(echo=obj.echo)

    def build(self, flow_graph: FlowGraph) -> Tuple[Workflow, List[PythonFunctionTask]]:
        self.echo(str(flow_graph))

        # Provided by @project decorator if present
        #
        # TODO: Require this?
        project: Optional[str] = current.get("project_name")
        domain: Optional[str] = current.get("branch_name")

        wf = Workflow(
            name=flow_graph.name,
        )
        self.echo("Adding hello-world dummy task")
        wf.add_entity(hello_world)

        self.echo("Ignoring all nodes in the workflow; stuff's WIP okay?")
        self.echo(f"Constructed shell Flyte workflow: {wf}")

        # TODO: package the workflow using the pyflyte cli bundled with Flytekit and upload it to the Flyte
        # backend.
        #
        # metaflow.plugins.aws.step_functions.step_functions_cli.make_flow might be useful ref here, e.g. its use of
        # MetaflowPackage
        #
        # Convert the Workflow to proto, upload via gRPC client?
        #
        # flytekit.extend.get_serializable to convert workflow object to IDL object
        return wf, [hello_world]
