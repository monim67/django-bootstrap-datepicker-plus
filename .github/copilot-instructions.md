# AI Coding Agent Instructions for django-bootstrap-datepicker-plus

## Project Overview
This is a Django package providing Bootstrap datepicker widgets (DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput) that integrate bootstrap-datetimepicker v4. Supports Bootstrap 3/4/5 with date-range functionality.

## Architecture
- **Core Components**: Widgets inherit from `BasePickerInput` (in `_base.py`), configured via `WidgetConfig` (Pydantic model in `_config.py`)
- **Configuration Flow**: Django settings (`BOOTSTRAP_DATEPICKER_PLUS`) → `WidgetSettings` (Pydantic BaseSettings) → widget options
- **Rendering**: Uses Django templates (`bootstrap_datepicker_plus/input.html`) with data attributes for JS initialization
- **Data Flow**: Widget options → JSON in `data-dbdp-config` attribute → JS bootstrap-datetimepicker

## Key Files
- `src/bootstrap_datepicker_plus/widgets.py`: Widget classes (variants: date/time/datetime/month/year)
- `src/bootstrap_datepicker_plus/_base.py`: Base widget logic, attrs building, context
- `src/bootstrap_datepicker_plus/_config.py`: Pydantic config merging options
- `src/bootstrap_datepicker_plus/settings.py`: Django settings integration with defaults
- `src/bootstrap_datepicker_plus/schemas.py`: Type definitions (WidgetVariant enum, WidgetOptions dict)

## Developer Workflows
- **Dependencies**: Use Poetry (`poetry install`, `poetry add`)
- **Testing**: `pytest` with pytest-django; fixtures in `tests/conftest.py` clear settings cache
- **Docs Build**: `poetry run make -C docs html` (Sphinx)
- **Dev Server**: `cd dev && python manage.py runserver` (includes demo forms)
- **Linting/Formatting**: Black for code formatting

## Conventions
- **Options Merging**: Settings → variant_options → widget.options → instance options (last wins)
- **Date Formats**: `_date_format` (Python strftime) vs `backend_date_format` (Moment.js)
- **Deprecations**: Use `typing_extensions.deprecated` decorator for old APIs
- **Pydantic Usage**: v2 with pydantic-settings for Django settings integration
- **Testing**: Use `SettingsWrapper` fixture to reset cached settings between tests

## Examples
- **Basic Widget**: `DatePickerInput(options={'format': 'YYYY-MM-DD'})`
- **Range Picker**: `DatePickerInput(range_from='start_date')` links inputs
- **Custom Settings**: `BOOTSTRAP_DATEPICKER_PLUS = {'options': {'locale': 'en'}}` in Django settings
- **Variant Options**: `BOOTSTRAP_DATEPICKER_PLUS['variant_options']['time'] = {'format': 'HH:mm'}`

## Integration Points
- **Django Forms**: Widgets used in ModelForm fields
- **Bootstrap Versions**: Static files served via settings URLs (CDN defaults)
- **External Deps**: moment.js, bootstrap-datetimepicker JS/CSS, bootstrap-icons CSS</content>
<parameter name="filePath">/Users/monim/monim67/django-bootstrap-datepicker-plus/.github/copilot-instructions.md