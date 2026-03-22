from __future__ import annotations

import importlib
from functools import lru_cache
from types import ModuleType


@lru_cache(maxsize=1)
def load_sg_module() -> ModuleType:
    """Load a compatible SimpleGUI module with required Tree support."""
    import_errors = []
    for module_name in ('PySimpleGUI', 'FreeSimpleGUI'):
        try:
            sg_module = importlib.import_module(module_name)
            if not hasattr(sg_module, 'Tree'):
                import_errors.append(f"{module_name}: missing Tree element")
                continue
            return sg_module
        except ImportError as e:
            import_errors.append(f"{module_name}: {e}")

    raise ImportError('; '.join(import_errors))
