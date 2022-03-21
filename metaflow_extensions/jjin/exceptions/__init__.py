from metaflow.exception import MetaflowException


class FlyteNotReadyException(MetaflowException):
    headline = "Flyte workflow not ready."

    def __init__(self):
        super().__init__(
            msg="Check that the generated Flyte workflow is valid and try again."
        )


class FlyteMissingProjectAndBranchException(MetaflowException):
    headline = "Missing project and branch"

    def __init__(self):
        super().__init__(msg="Please use @project on your flow and try again.")
