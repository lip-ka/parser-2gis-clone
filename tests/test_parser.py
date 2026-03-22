import csv
import json
import os
import sys
from tempfile import TemporaryDirectory

import pytest
from parser_2gis import main as parser_main
from parser_2gis.runner import cli as cli_runner


def check_csv_result(result_path, num_records):
    """Check CSV output.

    Args:
        file_path: Path to CSV table.
        num_records: Expected number of records.
    """
    with open(result_path, 'r', encoding='utf-8-sig', errors='replace') as f:
        # CSV writer uses `;` delimiter by default.
        reader = csv.reader(f, delimiter=';')
        assert len(list(reader)) == num_records + 1  # `num_records` + header


def check_csv_extended_fields(result_path):
    """Check extended CSV fields from existing model."""
    with open(result_path, 'r', encoding='utf-8-sig', errors='replace') as f:
        reader = csv.DictReader(f, delimiter=';')
        row = next(reader)

    assert row['Локаль'] == 'ru_RU'
    assert row['Алиас города'] == 'moscow'
    assert row['ID региона'] == 'region-1'
    assert row['ID сегмента'] == 'segment-1'
    assert row['ID организации'] == 'org-1'
    assert row['Название организации'] == 'Test Org'
    assert row['Количество филиалов организации'] == '5'
    assert row['Работает 24/7'] == 'True'
    assert row['Комментарий к расписанию'] == 'Ежедневно'
    assert row['Смещение часового пояса (мин)'] == '180'


def check_json_result(result_path, num_records):
    """Check JSON output.

    Args:
        file_path: Path to JSON file.
        num_records: Expected number of records.
    """
    with open(result_path, 'r', encoding='utf-8-sig', errors='replace') as f:
        doc = json.load(f)
        assert len(doc) == num_records


testdata = [
    ['csv', check_csv_result],
    ['json', check_json_result],
]


@pytest.mark.parametrize('format, result_checker', testdata)
def test_parser(monkeypatch, format, result_checker, num_records=5):
    """Parse TOP `num_records` entries and check result file.

    Args:
        format: Result format (`csv` or `json`).
        result_checker: Function that checks parsed result.
        num_records: Number of records to be parsed.
    """
    with monkeypatch.context() as m, TemporaryDirectory() as tmpdir:
        class DummyParser:
            def __init__(self, parser_options):
                self._parser_options = parser_options

            def __enter__(self):
                return self

            def __exit__(self, *exc_info):
                pass

            def parse(self, writer):
                for i in range(self._parser_options.max_records):
                    writer.write({
                        'meta': {'code': 200},
                        'result': {
                            'items': [{
                                'id': f'{i}_dummy',
                                'locale': 'ru_RU',
                                'type': 'firm',
                                'name': f'Test Item {i}',
                                'city_alias': 'moscow',
                                'region_id': 'region-1',
                                'segment_id': 'segment-1',
                                'timezone_offset': 180,
                                'org': {
                                    'id': 'org-1',
                                    'name': 'Test Org',
                                    'branch_count': 5,
                                },
                                'schedule': {
                                    'Mon': {'working_hours': [{'from': '09:00', 'to': '18:00'}]},
                                    'is_24x7': True,
                                    'comment': 'Ежедневно',
                                },
                                'contact_groups': [],
                                'adm_div': [],
                                'rubrics': [],
                            }]
                        }
                    })

        m.setattr(cli_runner, 'get_parser',
                  lambda url, chrome_options, parser_options: DummyParser(parser_options))

        result_path = os.path.join(tmpdir, f'output.{format}')

        m.setattr(sys, 'argv', [
            os.path.abspath(__file__),
            '-i', 'https://2gis.ru/moscow/search/Аптеки',
            '-o', result_path,
            '-f', format,
            '--parser.max-records', f'{num_records}',
            '--chrome.headless', 'yes',
        ])

        # Run parser on a popular query
        # that gotta have at least `num_records` records.
        parser_main()

        # Check parsed results
        result_checker(result_path, num_records)

        if format == 'csv':
            check_csv_extended_fields(result_path)
