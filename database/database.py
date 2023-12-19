from typing import TypeVar

import pypyodbc as odbc
from env import Environment


class Database:

    def __init__(self, database_name: str, model: object):
        self.database_name = database_name
        self.model = model

        self.DRIVER_NAME = Environment.DRIVER_NAME
        self.SERVER_NAME = Environment.SERVER_NAME
        self.DATABASE_NAME = Environment.DATABASE_NAME
        self.TRUST_CONNECTION = Environment.TRUST_CONNECTION

        self.connection_data = f"""
            DRIVER={{{self.DRIVER_NAME}}};
            SERVER={self.SERVER_NAME};
            DATABASE={self.DATABASE_NAME};
            Trust_Connection={self.TRUST_CONNECTION};
        """

        self.connection = odbc.connect(self.connection_data)

    def list(self):
        models = []
        cursor = self.connection.cursor()
        cursor.execute(f'SELECT * FROM {self.database_name}')
        for row in cursor:
            models.append(self.model(*list(row)))

        cursor.commit()
        return models

    def get_by_id(self, id: int):
        cursor = self.connection.cursor()
        cursor.execute(f'SELECT * FROM {self.database_name} WHERE ID = {id}')
        for row in cursor.fetchall():
            cursor.commit()
            return self.model(*list(row))

    def get_by_query(self, query: str):
        cursor = self.connection.cursor()
        cursor.execute(f'SELECT * FROM {self.database_name} WHERE {query}')
        for row in cursor.fetchall():
            cursor.commit()
            return self.model(*list(row))
