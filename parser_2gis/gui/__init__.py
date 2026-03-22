from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..config import Configuration


def gui_app(urls: list[str], output_path: str, format: str, config: 'Configuration') -> None:
    """Lazy proxy to avoid importing GUI modules at package import time.

    This prevents circular imports when checking GUI availability from
    ``parser_2gis.common`` via ``parser_2gis.gui.sg``.
    """
    from .app import gui_app as _gui_app

    return _gui_app(urls, output_path, format, config)


__all__ = [
    'gui_app',
]
