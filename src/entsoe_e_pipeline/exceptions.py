class PipelineError(Exception):
    """Base class for exceptions in the pipeline."""

    pass


class ExtractError(PipelineError):
    """Exception raised for errors during the extraction phase."""

    pass


class transformError(PipelineError):
    """Exception raised for errors during the transformation phase."""

    pass


class LoadError(PipelineError):
    """Exception raised for errors during the loading phase."""

    pass


class ConfigError(PipelineError):
    """Exception raised for errors in the configuration."""

    pass
