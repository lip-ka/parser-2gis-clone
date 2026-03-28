**Parser2GIS** - парсер сайта [2GIS](https://2gis.ru/) с помощью браузера [Google Chrome](https://google.com/chrome).

## ✨ Особенности
- 🤖 Успешно обходит анти-бот блокировки на территории РФ
- 🖥️ Работает под Windows, Linux и MacOS
- 📄 Два выходных формата: CSV таблица и JSON список
- 🔗 Наличие генератора ссылок по городам и рубрикам
- Работает только при выключенном VPN

## 🚀 Установка
> Для работы парсера необходимо установить браузер [Google Chrome](https://google.com/chrome).

### Установка одним файлом

  Скачать [последний релиз](https://github.com/lip-ka/parser-2gis-clone/releases/tag/v1.3.0) и выбрать артефакт под вашу ОС:
  - `Parser2GIS-<версия>-windows.zip` — Windows (`Parser2GIS.exe`)
  - `Parser2GIS-<версия>-linux.tar.gz` — Linux
  - `Parser2GIS-<версия>-macos.tar.gz` — MacOS (Intel)
  - `Parser2GIS-<версия>-macos-arm.tar.gz` — MacOS (Apple Silicon)

### Подробная инструкция по установке и запуску в **PyCharm на Windows**

В этом разделе полный, структурированный сценарий «с нуля» для Windows:
от скачивания проекта до стабильного запуска GUI/CLI и внесения правок в код.
Все команды в этом разделе предполагается выполнять во **встроенном локальном терминале PyCharm**.

#### 0) Что должно быть установлено заранее

1. **Git for Windows** (если планируете менять основной репозиторий на GitHub)
2. **Python 3.11.x** (рекомендуется)
3. **PyCharm** (Community или Professional)
4. **Google Chrome** (обязательно для работы парсера)

> Важно: используйте именно Python 3.11 и всегда ставьте пакеты через
> `python -m pip ...`, а не просто `pip ...`.
> Это защищает от типичной ошибки, когда `pip` ставит зависимости в другой Python.

##### 0.1 Как установить Python 3.11 на Windows (подробно)

1. Перейдите на официальный сайт Python: **https://www.python.org/downloads/windows/**.
2. В блоке Python 3.11 скачайте установщик:
   - обычно это `Windows installer (64-bit)` (`python-3.11.x-amd64.exe`).
3. Сохраните файл установщика в удобную папку, например:
   - `C:\Users\<you>\Downloads\`
   - или `C:\Installers\Python\`

> Куда «складывать» файл установщика не критично: это временный `.exe`, который нужен только для установки.
> После успешной установки его можно оставить в архивной папке (`C:\Installers\...`) или удалить.

4. Запустите скачанный `.exe` от имени обычного пользователя.
5. На первом экране установки **обязательно** включите:
   - `Add python.exe to PATH`
6. Нажмите `Customize installation` (рекомендуется), затем `Next`.
7. На шаге `Advanced Options` оставьте включённым:
   - `Install for all users` (по желанию),
   - `Add Python to environment variables`,
   - `Associate files with Python`.
8. Завершите установку.

##### 0.2 Как установить PyCharm на Windows (подробно)

1. Откройте ссылку на скачивание PyCharm:
   - **https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows**
2. Дождитесь загрузки установщика (`.exe`).
3. Сохраните установщик в удобное место, например:
   - `C:\Users\<you>\Downloads\`
   - `C:\Installers\JetBrains\`
4. Запустите установщик PyCharm.
5. На шаге установки (Installation Options) рекомендуется:
   - включить `Add "bin" folder to the PATH`;
   - включить ассоциацию `.py` с PyCharm (по желанию);
   - включить `Create Desktop Shortcut` (по желанию).
6. Завершите установку и запустите PyCharm.
7. При первом старте:
   - выберите тему/настройки интерфейса;
   - при необходимости войдите в JetBrains Account;
   - дождитесь инициализации IDE.

Проверка, что python установился корретно 

(во встроенном терминале PyChar):

```cmd
py -3.11 --version
py -0p
```

Ожидаемо:
- первая команда показывает `Python 3.11.x`;
- вторая показывает список установленных Python и путь к `Python311\python.exe`.

Если `py` не найден:

```cmd
python --version
where python
```

В этом случае проверьте, что Python добавлен в PATH, или переустановите Python с галочкой `Add python.exe to PATH`.

Проверка, что всё установилось корректно:

1. PyCharm запускается без ошибок.
2. В меню доступны:
   - **Get from VCS** (для клонирования репозитория),
   - **File → Settings → Project → Python Interpreter** (для настройки Python 3.11).

---

#### 1) Скачивание репозитория в PyCharm

1. Откройте PyCharm.
2. Нажмите **Get from VCS**.
3. Вставьте URL репозитория:
   - SSH: `git@github.com:lip-ka/parser-2gis-clone.git`
   - HTTPS: `https://github.com/lip-ka/parser-2gis-clone.git`
4. Выберите папку, например `C:\Users\<you>\PycharmProjects\parser-2gis-clone`.
5. Нажмите **Clone**.
---

#### 2) Создание и подключение интерпретатора Python 3.11

1. В PyCharm: **File → Settings → Project → Python Interpreter**.
2. Нажмите **Add Interpreter**.
3. Выберите:
   - **Add Local Interpreter**
   - **Virtualenv Environment**
   - **New**
4. Укажите:
   - `Base interpreter`: путь к `Python311\python.exe` -- то место, куда вы сохранили Python 3.11 на подготовительном шаге
   - `Location`: `<project>\.venv`
5. Нажмите **OK / Apply**.

Подсказка по пути `Base interpreter`:
- чаще всего это `C:\Users\<you>\AppData\Local\Programs\Python\Python311\python.exe`;
- если ставили `Install for all users`, путь может быть `C:\Program Files\Python311\python.exe`.

Если кнопка **OK** неактивна:
- проверьте, что `Base interpreter` выбран;
- укажите новый (не существующий) путь для venv;
- попробуйте путь без кириллицы/пробелов;
- или создайте venv вручную (см. шаг 3).

---

#### 3) Создание venv вручную (если удобнее)

Во встроенном терминале PyCharm:

```cmd
py -3.11 -m venv .venv
.venv\Scripts\activate
python --version
```

После этого в PyCharm можно выбрать **Existing interpreter**:
`<project>\.venv\Scripts\python.exe`.

---

#### 4) Проверка, что `python` и `pip` смотрят в один интерпретатор

Обязательная проверка перед установкой зависимостей:

```cmd
python -c "import sys; print('PYTHON =', sys.executable)"
python -m pip -V
```

Если пути отличаются — выбран не тот интерпретатор.

---

#### 5) Установка зависимостей проекта

Ввести команды во встроенный терминал

Базовые (CLI). 

```cmd
python -m pip install --upgrade pip
python -m pip install -e .
```

GUI-зависимости:

```cmd
python -m pip install -e ".[gui]"
```

Проверка:

```cmd
python -m pip show pydantic
python -m pip show FreeSimpleGUI PySimpleGUI
```

---

#### 6) Настройка Run/Debug Configuration в PyCharm

Рекомендуется сделать **две** конфигурации.

##### 6.1 GUI-конфигурация (обычная работа через окно)

- **Type**: Python
- **Run kind**: Script path
- **Script path**: `<project>\parser-2gis.py`
- **Parameters**: пусто
- **Working directory**: корень проекта
- **Interpreter**: `<project>\.venv\Scripts\python.exe`

Запуск:

```cmd
python parser-2gis.py
```

##### 6.2 CLI-конфигурация (быстрые тестовые прогоны)

- **Type**: Python
- **Run kind**: Script path
- **Script path**: `<project>\parser-2gis.py`
- **Working directory**: корень проекта
- **Interpreter**: `<project>\.venv\Scripts\python.exe`
- **Parameters** (пример JSON-выгрузки):

```text
-i "https://2gis.ru/moscow/search/кофе" -o "output/result.json" -f json --chrome.headless yes --parser.max-records 200 --writer.verbose yes
```

Обязательные параметры CLI: `-i`, `-o`, `-f`.

---

#### 7) Форматы результата и примеры команд

- CSV: `-f csv -o output/result.csv`
- XLSX: `-f xlsx -o output/result.xlsx`
- JSON: `-f json -o output/result.json`

Пример JSON:

```cmd
python parser-2gis.py -i "https://2gis.ru/moscow/search/кофе" -o "output/result.json" -f json
```

---

#### 8) Что обязательно сделать перед первым запуском

Создайте папку для результатов, чтобы избежать `FileNotFoundError`:

```cmd
mkdir output
```

---

#### 9) Диагностика, если «зависает» или «не запускается»

1. Для диагностики запускайте так:
   - `--chrome.headless no`
   - `--chrome.silent-browser no`
   - `--parser.max-records 10`
2. Временно выключите VPN/Proxy.
3. Проверьте, что Chrome открывается вручную и доступен интернет.
4. Убедитесь, что в PyCharm выбран именно `.venv` проекта.

---

#### 10) Частые ошибки и быстрые решения

##### `ModuleNotFoundError: No module named pydantic`

```cmd
python -m pip install -e .
python -m pip show pydantic
```

##### `pip` не найден

```cmd
py -m pip --version
```

или:

```cmd
python -m pip --version
```

##### Предупреждение `RuntimeWarning: 'parser_2gis.main' found in sys.modules ...`

Запускайте через script `parser-2gis.py` (как в конфигурации выше), а не через `-m parser_2gis.main`.

##### GUI не стартует

```cmd
python -m pip install -e ".[gui]"
python -m pip show FreeSimpleGUI PySimpleGUI
```

---

#### 11) Рекомендуемый рабочий процесс (локальная разработка) (тут уже нужен git)

1. Создайте ветку:

```cmd
git checkout -b feature/<short-name>
```

2. Внесите правки в код.
3. Запустите GUI/CLI и проверьте результат.
4. Сделайте commit.
5. Отправьте ветку в GitHub и создайте Pull Request.
## 📖 Документация
Описание работы доступно на [вики](https://github.com/lip-ka/parser-2gis-clone/wiki).


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
