from __future__ import annotations

from functools import lru_cache
from types import ModuleType


@lru_cache(maxsize=1)
def load_sg_module() -> ModuleType:
    """Load a compatible SimpleGUI module with required Tree support."""
    import_errors = []
    for module_name in ('PySimpleGUI', 'FreeSimpleGUI'):
        try:
            if module_name == 'PySimpleGUI':
                import PySimpleGUI as sg_module
            else:
                import FreeSimpleGUI as sg_module

            if not hasattr(sg_module, 'Tree'):
                import_errors.append(f"{module_name}: missing Tree element")
                continue

            return sg_module
        except ImportError as e:
            import_errors.append(f"{module_name}: {e}")

    raise ImportError('; '.join(import_errors))
