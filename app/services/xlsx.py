import xlsxwriter

from datetime import datetime
from pathlib import Path
from xlsxwriter.workbook import Workbook
from xlsxwriter.worksheet import Worksheet

from app.core.config import SPREADSHEETS_DIR


class ExportXLSXService:
    def create_summary_xlsx(self, data) -> Path:
        
        timestamp: str = datetime.now().strftime(format = "%d-%m-%Y_%H-%M-%S")
        path: Path = SPREADSHEETS_DIR / f"summary_{timestamp}.xlsx"

        workbook: Workbook = xlsxwriter.Workbook(filename = str(path))
        sheet: Worksheet = workbook.add_worksheet(name = "Summary")

        sheet.write(0, 0, "Category")
        sheet.write(0, 1, "Label")
        sheet.write(0, 2, "Value")
        sheet.write(0, 3, "Frequency")

        row: int = int(1)

        for category, rows in data.items():
            sheet.write(row, 0, category)
            row += 1

            for item in rows:
                sheet.write(row, 1, item["label"])
                sheet.write(row, 2, item["value"])
                sheet.write(row, 3, item["frequency"])
                row += 1

            row += 1

        workbook.close()
        return path