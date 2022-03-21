from .flyte import flyte_cli
from .foo import FooDecorator


def get_plugin_cli():
    return [flyte_cli.cli]


FLOW_DECORATORS = [
    FooDecorator,
]
