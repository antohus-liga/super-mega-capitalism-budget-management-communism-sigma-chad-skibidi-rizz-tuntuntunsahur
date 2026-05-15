import sqlite3 # TODO: implement the necessary code to create the database, /
#  connect and make changes to it


class Database:
    def __init__(self) -> None:
        pass
    def connect(self) -> None:
        pass
    def create_tables(self) -> None:
        """
                CREATE TABLE IF NOT EXISTS budget(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name TEXT NOT NULL,
                price REAL NOT NULL,
                date TEXT NOT NULL
            )
        """ # date should be stored as TEXT type because it is the /
        # correct way to do it in SQLite 3 e.g. "DD-MM-YYYY" as it is /
        # stated on its documentation that it does not have native support /
        # for the DATE type