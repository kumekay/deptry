from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from pathlib import Path


class ProjectBuilder(Protocol):
    def __call__(self, project: str, setup_command: str, cwd: str | None) -> Path:
        ...


class ToolSpecificProjectBuilder(Protocol):
    def __call__(self, project: str, cwd: str | None = None) -> Path:
        ...
