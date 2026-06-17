from typing import Protocol

class SupportsRowsData(Protocol):
    def get_rows_data(self) -> list[dict]:
        ...