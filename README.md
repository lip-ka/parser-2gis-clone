<p align="center">
  <a href="#%E2%84%B9%EF%B8%8F-%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5">
    <img alt="Logo" width="128" src="https://user-images.githubusercontent.com/20641837/174094285-6e32eb04-7feb-4a60-bddf-5a0fde5dba4d.png"/>
  </a>
</p>
<h1 align="center">Parser2GIS</h1>

<p align="center">
  <a href="https://github.com/interlark/parser-2gis/actions/workflows/tests.yml"><img src="https://github.com/interlark/parser-2gis/actions/workflows/tests.yml/badge.svg" alt="Tests"/></a>
  <a href="https://pypi.org/project/parser-2gis"><img src="https://badgen.net/pypi/v/parser-2gis" alt="PyPi version"/></a>
  <a href="https://pypi.org/project/parser-2gis"><img src="https://badgen.net/pypi/python/parser-2gis" alt="Supported Python versions"/></a>
  <a href="https://github.com/interlark/parser-2gis/releases"><img src="https://img.shields.io/github/downloads/interlark/parser-2gis/total.svg" alt="Downloads"/></a>
</p>

**Parser2GIS** - парсер сайта [2GIS](https://2gis.ru/) с помощью браузера [Google Chrome](https://google.com/chrome).

<img alt="Screenshot" src="https://user-images.githubusercontent.com/20641837/174098241-7c0874aa-e70d-4978-86dc-7fd90af44603.png"/>

## ℹ️ Описание

Парсер для автоматического сбора базы адресов и контактов предприятий, которые работают на территории
России <img width="18px" src="https://user-images.githubusercontent.com/20641837/183511175-3d47f0f0-4e3f-45d2-8495-95d0612a8a8c.svg"/>, Казахстана <img width="18px" src="https://user-images.githubusercontent.com/20641837/183511625-20420aef-59c3-426d-a112-654d2caf0dda.svg"/>, Беларуси <img width="18px" src="https://user-images.githubusercontent.com/20641837/183511940-ce088ad1-d97f-4fa1-849a-9b887ad481c5.svg"/>,
Азербайджана <img width="18px" src="https://user-images.githubusercontent.com/20641837/183512176-1f6795a1-ceac-4865-a29f-b5720ce5115e.svg"/>, Киргизии <img width="18px" src="https://user-images.githubusercontent.com/20641837/183512234-286ca403-5194-4a6d-a59e-59201140078a.svg"/>, Узбекистана <img width="18px" src="https://user-images.githubusercontent.com/20641837/183512333-7ec1f36d-07fe-450d-b6f1-eed59a3b69c8.svg"/>, Чехии <img width="18px" src="https://user-images.githubusercontent.com/20641837/183512458-5a5d9531-a8f0-4624-99da-7069cde84926.svg"/>, Египта <img width="18px" src="https://user-images.githubusercontent.com/20641837/183512581-71fa2106-8cc1-43cc-a680-b3ff420acb8a.svg"/>, Италии <img width="18px" src="https://user-images.githubusercontent.com/20641837/183512763-0b438e5b-3ff0-4717-a826-0baac9207167.svg"/>, Саудовской Аравии <img width="18px" src="https://user-images.githubusercontent.com/20641837/183512980-427a985a-df1b-42c8-90bb-2c61692b6654.svg"/>, Кипра <img width="18px" src="https://user-images.githubusercontent.com/20641837/183513128-4367d2b1-feb9-4efe-bc57-73a15d178ef2.svg"/>, Объединенных Арабских Эмиратов <img width="18px" src="https://user-images.githubusercontent.com/20641837/183513374-9afef8c7-923e-4a18-9cd8-c69645b99377.svg"/>, Чили <img width="18px" src="https://user-images.githubusercontent.com/20641837/183513576-7209ce90-a04a-4258-9832-ef210198c3c4.svg"/>, Катара <img width="18px" src="https://user-images.githubusercontent.com/20641837/183513757-143ee2bf-b66c-4766-bbe1-db896a33eac1.svg"/>, Омана <img width="18px" src="https://user-images.githubusercontent.com/20641837/183513865-27509b74-b08f-4d92-b83b-a0d3aaabe155.svg"/>, Бахрейна <img width="18px" src="https://user-images.githubusercontent.com/20641837/183514076-3b6c9496-7c95-4452-8ee1-8723d98f876d.svg"/>, Кувейта <img width="18px" src="https://user-images.githubusercontent.com/20641837/183514240-7eff8632-5cd2-46ac-bed4-e483bb2df5f0.svg"/>.

## ✨ Особенности
- 💰 Абсолютно бесплатный
- 🤖 Успешно обходит анти-бот блокировки на территории РФ
- 🖥️ Работает под Windows, Linux и MacOS
- 📄 Три выходных формата: CSV таблица, XLSX таблица и JSON список
- 🔗 Наличие генератора ссылок по городам и рубрикам
- Работает только при выключенном VPN

## 🚀 Установка
> Для работы парсера необходимо установить браузер [Google Chrome](https://google.com/chrome).

### Установка одним файлом

  Скачать [последний релиз](https://github.com/interlark/parser-2gis/releases/latest) и выбрать артефакт под вашу ОС:
  - `Parser2GIS-<версия>-windows.zip` — Windows (`Parser2GIS.exe`)
  - `Parser2GIS-<версия>-linux.tar.gz` — Linux
  - `Parser2GIS-<версия>-macos.tar.gz` — MacOS (Intel)
  - `Parser2GIS-<версия>-macos-arm.tar.gz` — MacOS (Apple Silicon)

  Релизы публикуются автоматически после пуша тега вида `vX.Y.Z` и сразу доступны для скачивания внешним пользователям.

### Установка из PyPI
  ```bash
  # CLI
  pip install parser-2gis
  # CLI + GUI
  pip install parser-2gis[gui]
  ```

### Локальный запуск проекта (для разработки в PyCharm)

Рекомендуется использовать отдельное виртуальное окружение и устанавливать зависимости через `python -m pip`,
чтобы `pip` и интерпретатор проекта всегда совпадали.

```bash
# Создать и активировать venv
python -m venv .venv
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
# Linux/MacOS
source .venv/bin/activate

# Установить зависимости проекта
python -m pip install --upgrade pip
python -m pip install -e .
```

Для запуска GUI дополнительно установите GUI-зависимости:

```bash
python -m pip install -e ".[gui]"
```

После этого GUI можно запускать без обязательных CLI-аргументов:

```bash
python parser-2gis.py
```

Если хотите запускать CLI, укажите параметры `-i`, `-o`, `-f`.

## 📖 Документация
Описание работы доступно на [вики](https://github.com/interlark/parser-2gis/wiki).

## 🧠 Где находится ядро парсинга

Если нужно понять, где извлекаются поля и как формируется CSV/XLSX/JSON:

- `parser_2gis/parser/parsers/main.py` — основной сценарий прохода по страницам поиска 2GIS,
  клик по карточкам и получение JSON-ответов `catalog.api.2gis.../items/byid`.
- `parser_2gis/parser/parsers/in_building.py` и `parser_2gis/parser/parsers/firm.py` — вариации
  парсера для URL форматов `inside/...` и `firm/...`.
- `parser_2gis/writer/writers/csv_writer.py` — маппинг полей API в колонки CSV
  (`_data_mapping`) и извлечение значений (`_extract_raw`).
- `parser_2gis/writer/models/catalog_item.py` + `parser_2gis/writer/models/*.py` — схема
  структуры API-документа (через Pydantic), с которой работает writer.

Именно связка `*_parser.py` (получение JSON) + `csv_writer.py`/`xlsx_writer.py` (раскладка по колонкам)
является «ядром», которое стоит проверять первым при изменениях структуры 2GIS.

## 👍 Поддержать проект
<a href="https://yoomoney.ru/to/4100118362270186" target="_blank">
  <img alt="Yoomoney Donate" src="https://github.com/interlark/parser-2gis/assets/20641837/e875e948-0d69-4ed5-804c-8a1736ab0c9d" width="150">
</a>
