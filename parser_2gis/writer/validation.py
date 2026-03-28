from __future__ import annotations

import os


def validate_output_path_format(output_path: str, file_format: str) -> None:
    """Validate output file path extension against selected file format.

    Args:
        output_path: Path to output file.
        file_format: Expected file format (`csv`, `xlsx`, `json`).

    Raises:
        ValueError: If output path extension doesn't match format or if extension is missing.
    """
    if file_format not in ('csv', 'xlsx', 'json'):
        raise ValueError('Формат результирующего файла должен быть csv, xlsx или json!')

    ext = os.path.splitext(output_path)[1].lower().lstrip('.')
    if ext != file_format:
        raise ValueError('Расширение результирующего файла должно быть *.%s!' % file_format)
