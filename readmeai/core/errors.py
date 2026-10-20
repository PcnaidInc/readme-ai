from __future__ import annotations




class ReadmeAIError(Exception):
    """
    Base class for exceptions in this module.
    """

    ...


class ReadmeGeneratorError(Exception):
    """
    Raised when an error occurs during README generation.
    """

    def __init__(self, message: str):
        self.message = f"Error generating README: {message}"
        super().__init__(self.message)


# ----------------- CLI ----------------------------------


class CLIError(ReadmeAIError):
    """Exceptions related to the CLI."""

    def __init__(self, message: str):
        super().__init__(f"Invalid option provided to CLI: {message}")


# ----------------- File System ----------------------------------


class FileSystemError(ReadmeAIError):
    """
    Exceptions related to file system operations.
    """

    def __init__(self, message: str):
        super().__init__(f"File system error: {message}")


class FileReadError(FileSystemError):
    """
    Raised when a file cannot be read.
    """

    ...


class FileWriteError(FileSystemError):
    """
    Raised when a file cannot be written to.
    """

    ...


# ----------------- Git ----------------------------------


class GitValidationError(ReadmeAIError):
    """
    Base class errors validating Git repositories.
    """

    ...


class GitCloneError(GitValidationError):
    """
    Raised when a Git repository cannot be cloned.
    """

    def __init__(self, repository: str):
        self.repository = repository
        super().__init__(f"Failed to clone repository: {repository}")


class GitURLError(GitValidationError):
    """
    Raised when an invalid Git repository URL is provided.
    """

    def __init__(self, url: str):
        self.url = url
        super().__init__(f"Invalid Git repository URL: {url}")


class InvalidRepositoryError(GitValidationError):
    """
    Raised when an invalid repository is provided.
    """

    def __init__(self, repository: str):
        self.repository = repository
        super().__init__(f"Invalid repository provided: {repository}")


class UnsupportedGitHostError(GitValidationError):
    """
    Raised when an unsupported Git host is provided.
    """

    def __init__(self, host: str):
        self.host = host
        super().__init__(f"Unsupported Git host: {host}")


# ----------------- Repository ----------------------------------


class RepositoryProcessingError(ReadmeAIError):
    """
    Raised when an error occurs during repository processing.
    """

    ...


# ----------------- LLM API ----------------------------------


class UnsupportedServiceError(ReadmeAIError):
    """
    Raised when an unsupported LLM service is provided.
    """

    def __init__(self, message: str):
        super().__init__(message)
