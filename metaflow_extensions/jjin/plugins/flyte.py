from metaflow.decorators import FlowDecorator


class FlyteDecorator(FlowDecorator):
    name = "flyte"
    defaults = {"project": None, "domain": None}

    def flow_init(
        self, flow, graph, environment, flow_datastore, metadata, logger, echo, options
    ):
        echo(
            f"@flyte project: *{self.attributes.get('project')}*, domain: *{self.attributes.get('domain')}*",
            fg="magenta",
            highlight="green",
        )
