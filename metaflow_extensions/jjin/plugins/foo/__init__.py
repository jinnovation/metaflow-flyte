from metaflow.decorators import FlowDecorator


class FooDecorator(FlowDecorator):
    name = "foo"

    def flow_init(
        self,
        flow,
        graph,
        environment,
        flow_datastore,
        metadata,
        logger,
        echo,
        options,
    ):
        echo(
            "Testing testing 1 2 3",
            fg="magenta",
            highlight="green",
        )
