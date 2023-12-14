import sqlite3
from itertools import compress
import datetime


def execute(func):
    def f(self, *args, **kwargs):
        func(self, *args, **kwargs)
        return self.executor()

    return f

def strict(func):
    def f(self, *args, strict=False, **kwargs):
        func(self, *args, **kwargs)
        if strict:
            self.params = tuple([el.strip("%") for el in self.params])
    return f


class Table:
    def __init__(self, database: str):
        self.database = database
        with sqlite3.connect(database) as connection:
            self.connection = connection
            self.cursor = connection.cursor()
            self._create_table()

    def _create_table(self):
        self._sql_table_init()
        self.cursor.execute(self.s)
        self.connection.commit()

    def _sql_table_init(self):
        raise NotImplementedError()

    def executor(self):
        print(self.query, self.params)
        with sqlite3.connect(self.database) as connection:
            self.connection = connection
            self.cursor = connection.cursor()
            self.cursor.execute(self.query, self.params)
            return self.cursor.fetchall()


class Purchase(Table):

    def _sql_table_init(self):
        self.s = """       
        CREATE TABLE IF NOT EXISTS Purchase (
            id INTEGER PRIMARY KEY,
            is_done BIT,
            subject TEXT,
            description_short TEXT,
            description TEXT,
            deadline TEXT,
            dt TEXT
        )"""

    @execute
    def select_all(self):
        self.query = """
        SELECT Purchase.deadline, Purchase.description, Purchase.description_short, Purchase.subject, Purchase.is_done, Purchase.dt
        FROM Purchase 
        """

    @execute
    def insert(self, deadline, description, description_short, subject, is_done, dt):
        self.query = """INSERT INTO Purchase (dt, deadline, description, description_short, subject, is_done) 
                        VALUES (?, ?, ?, ?, ?, ?)"""
        self.params = (deadline, description, description_short, subject, is_done, dt)


class App:
    def __init__(self, database):
        self.p = Purchase(database)

    def add_purchase(self, deadline, description, description_short, subject, is_done, dt = None):
        if dt is None:
            dt = datetime.datetime.now().isoformat()
        self.p.insert(deadline, description, description_short, subject, is_done, dt)

    def get_statistic(self):
        """
        Выбор из таблицу Purchase строчек отвечающих данным параметрам
        """
        return self.p.select_all()