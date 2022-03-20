from metaflow import FlowSpec, project, step

# from metaflow import flyte


# FIXME: With flyte plugin CLI, specific decorator might not even be necessary.
# @flyte
@project(name="jjin_metaflow_flyte_project")
class SkeletonFlow(FlowSpec):
    """A flow that contains literally only a `start` and an `end`. It has no logic,
    no external dependencies, no resource requirements -- nothing.

    """

    @step
    def start(self):
        """Prints a message stating that the flow is starting. That's it."""
        print("SkeletonFlow is starting.")
        self.next(self.end)

    @step
    def end(self):
        """Prints a message stating that the flow is ending. That's it."""
        print("SkeletonFlow is ending.")


if __name__ == "__main__":
    SkeletonFlow()
