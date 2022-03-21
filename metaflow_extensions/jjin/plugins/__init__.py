from .flyte import flyte_cli


def get_plugin_cli():
    return [flyte_cli.cli]
