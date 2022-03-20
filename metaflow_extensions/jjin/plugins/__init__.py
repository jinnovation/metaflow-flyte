from .flyte import flyte_cli
from .flyte.decorators import FlyteDecorator


def get_plugin_cli():
    return [flyte_cli.cli]


FLOW_DECORATORS = [
    FlyteDecorator,
]
