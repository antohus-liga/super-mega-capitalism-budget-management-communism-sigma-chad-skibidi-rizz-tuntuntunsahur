import json

from pathlib import Path
from typing import cast, TypeAlias


JsonValue: TypeAlias = str | list[str]
JsonDict: TypeAlias = dict[str, JsonValue]


class TranslationService:
    def __init__(self, lang: str) -> None:
        self.lang: str = lang
        self.data: JsonDict = self._load_language_file(lang)

    def _load_language_file(self, lang: str) -> JsonDict:
        path: Path = Path("src/locales") / f"{lang}.json"

        if not path.exists():
            path = Path("src/locales") / "en_GB.json"  # fallback

        with open(file = path, mode = "r", encoding = "utf-8") as f:
            loaded: JsonDict = cast(JsonDict, json.load(fp = f))
            return loaded

    def get(self, key: str) -> JsonValue | None:
        return self.data.get(key)

    def get_list(self, key: str) -> list[str]:
        value: JsonValue | None = self.data.get(key)
        if isinstance(value, list):
            return value
        raise TypeError(
        f"Expected list[str] for key '{key}', got {type(value)}")