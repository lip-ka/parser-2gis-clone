import csv
import os
import sys
from tempfile import TemporaryDirectory

import pytest

from parser_2gis import main as parser_main
from parser_2gis.cli.app import cli_app
from parser_2gis.config import Configuration
from parser_2gis.runner import cli as cli_runner
from parser_2gis.writer.validation import validate_output_path_format


def test_validate_output_path_format():
    validate_output_path_format('out.csv', 'csv')
    validate_output_path_format('out.xlsx', 'xlsx')
    validate_output_path_format('out.JSON', 'json')

    with pytest.raises(ValueError, match=r'\*\.csv'):
        validate_output_path_format('out.xlsx', 'csv')

    with pytest.raises(ValueError, match=r'\*\.xlsx'):
        validate_output_path_format('out.csv', 'xlsx')

    with pytest.raises(ValueError, match='csv, xlsx или json'):
        validate_output_path_format('out.csv', 'xml')


def test_cli_app_rejects_mismatched_extension():
    config = Configuration()
    with pytest.raises(ValueError, match=r'\*\.csv'):
        cli_app(['https://2gis.ru/moscow/search/Аптеки'], 'result.xlsx', 'csv', config)


def test_cli_delimiter_argument(monkeypatch):
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
                                'contact_groups': [],
                                'adm_div': [],
                                'rubrics': [],
                            }]
                        }
                    })

        m.setattr(cli_runner, 'get_parser',
                  lambda url, chrome_options, parser_options: DummyParser(parser_options))

        result_path = os.path.join(tmpdir, 'output.csv')
        m.setattr(sys, 'argv', [
            os.path.abspath(__file__),
            '-i', 'https://2gis.ru/moscow/search/Аптеки',
            '-o', result_path,
            '-f', 'csv',
            '--parser.max-records', '3',
            '--chrome.headless', 'yes',
            '--writer.csv.delimiter', ',',
        ])

        parser_main()

        with open(result_path, 'r', encoding='utf-8-sig', errors='replace') as f:
            reader = csv.reader(f, delimiter=',')
            assert len(list(reader)) == 4
