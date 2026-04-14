# yaml_frontmatter:
#   id: 'error_handling'
#   script_path: 'scripts/core/error_handling.py'
#   metadata_path: 'metadata/scripts/core/error_handling.meta.json'
#   source_of_truth: 'metadata/scripts/**/*.meta.json'
#   title: 'Modelo de errores y colector para el pipeline'
#   key_functions:
#     - 'ErrorCollector.add'
#     - 'ErrorCollector.add_message'
#     - 'ErrorCollector.format_summary'
#   tags:
#     - 'errores'
#     - 'pipeline'
#     - 'diagnostico'

from dataclasses import dataclass
from typing import Any


class MathKernelError(Exception):
    """Error base del dominio MathKernel con contexto opcional."""

    def __init__(self, message: str, context: dict[str, Any] | None = None):
        super().__init__(message)
        self.message = message
        self.context = context or {}


class ValidationError(MathKernelError):
    """Error especializado para fallos de validacion."""

    pass


class FileOperationError(MathKernelError):
    """Error especializado para operaciones de archivo/directorio."""

    pass


class ProcessingError(MathKernelError):
    """Error especializado para pasos de procesamiento."""

    pass


@dataclass
class CollectedError:
    """Representa una incidencia recolectada durante la ejecucion."""

    step: str
    error_type: str
    message: str
    critical: bool = False


class ErrorCollector:
    """Acumula errores con severidad para reporte final uniforme."""

    def __init__(self) -> None:
        self.errors: list[CollectedError] = []

    def add(self, step: str, error: Exception, critical: bool = False) -> None:
        """Registra una excepcion preservando tipo y severidad."""

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
        """Registra un mensaje de error sintetico sin excepcion asociada."""

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
        """Indica si existe al menos una incidencia registrada."""

        return bool(self.errors)

    @property
    def has_critical_errors(self) -> bool:
        """Indica si hay incidencias criticas en el acumulado."""

        return any(item.critical for item in self.errors)

    def format_summary(self) -> list[str]:
        """Genera lineas de resumen listas para logging."""

        lines: list[str] = []
        for item in self.errors:
            level = "CRITICAL" if item.critical else "ERROR"
            lines.append(f"[{level}] {item.step}: {item.error_type} - {item.message}")
        return lines
