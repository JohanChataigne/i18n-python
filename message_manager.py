import json
from pathlib import Path

from icu import Locale, MessageFormat, Formattable


class MessageManager:
    _default_locale: Locale
    _messages: dict[Locale, dict[str, str]]
    _messages_directory: Path

    def __init__(self, messages_directory: Path, default_locale: Locale):
        self._default_locale = default_locale
        self._messages_directory = messages_directory

        self._messages = {}
        self._load_messages(default_locale)


    def get(self, key: str, locale: Locale, **kwargs) -> str:
        messages = self._messages.get(locale) or self._load_messages(locale=locale)

        if not key in messages:
            raise KeyError(f"Key {key} not found for locale {locale}")

        template = MessageFormat(messages[key], locale)
        variable_names = []
        variable_values = []

        for name, value in kwargs.items():
            variable_names.append(name)
            variable_values.append(Formattable(value))

        return template.format(variable_names, variable_values)

    def _load_messages(self, locale: Locale) -> dict[str, str]:
        messages_filepath = self._messages_directory / f"{locale.getName()}.json"
        messages = json.loads(messages_filepath.read_text())

        self._messages[locale] = messages

        return messages