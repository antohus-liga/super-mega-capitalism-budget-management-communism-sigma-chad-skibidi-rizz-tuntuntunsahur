
class Database:
    def __init__(self, name: str):
        self.name = name
        self.connection()
        self.tables()

    def connection(self):
       self.connect = sql.connect(self.name)
    def tables(self):
        cursor = self.connect.cursor()
        cursor.execute("""
            Create table if not exists produtos(
                id integer primary key autoincrement, 
                nome text not null,
                preco float not null
            )
        """)
