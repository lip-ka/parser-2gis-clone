from __future__ import annotations

from typing import TYPE_CHECKING

from ..logger import setup_cli_logger
from ..runner import CLIRunner
from ..writer import validate_output_path_format

if TYPE_CHECKING:
    from ..config import Configuration


def cli_app(urls: list[str], output_path: str, format: str, config: Configuration) -> None:
    setup_cli_logger(config.log)
    validate_output_path_format(output_path, format)

    runner = CLIRunner(urls, output_path, format, config)
    runner.start()
