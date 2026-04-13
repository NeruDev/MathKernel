from dataclasses import dataclass
from typing import Any


class MathKernelError(Exception):
    def __init__(self, message: str, context: dict[str, Any] | None = None):
        super().__init__(message)
        self.message = message
        self.context = context or {}


class ValidationError(MathKernelError):
    pass


class FileOperationError(MathKernelError):
    pass


class ProcessingError(MathKernelError):
    pass


@dataclass
class CollectedError:
    step: str
    error_type: str
    message: str
    critical: bool = False


class ErrorCollector:
    def __init__(self) -> None:
        self.errors: list[CollectedError] = []

    def add(self, step: str, error: Exception, critical: bool = False) -> None:
        if isinstance(error, MathKernelError):
            message = error.message
            error_type = error.__class__.__name__
        else:
            message = str(error)
            error_type = error.__class__.__name__

        self.errors.append(
            CollectedError(
                step=step,
                error_type=error_type,
                message=message,
                critical=critical,
            )
        )

    def add_message(self, step: str, message: str, critical: bool = False) -> None:
        self.errors.append(
            CollectedError(
                step=step,
                error_type="MessageError",
                message=message,
                critical=critical,
            )
        )

    @property
    def has_errors(self) -> bool:
        return bool(self.errors)

    @property
    def has_critical_errors(self) -> bool:
        return any(item.critical for item in self.errors)

    def format_summary(self) -> list[str]:
        lines: list[str] = []
        for item in self.errors:
            level = "CRITICAL" if item.critical else "ERROR"
            lines.append(f"[{level}] {item.step}: {item.error_type} - {item.message}")
        return lines
