import datetime
from typing import TypeVar, List

import pypyodbc as odbc
from env import Environment
from models import ServiceModel, ServicePhotoModel


class Database:

    def __init__(self, *, table_name: str, model: object):
        self.table_name = table_name
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
        cursor.execute(f'SELECT * FROM {self.table_name}')
        for row in cursor:
            models.append(self.model(*list(row)))

        cursor.commit()
        return models

    def get_by_id(self, id: int):
        cursor = self.connection.cursor()
        cursor.execute(f'SELECT * FROM {self.table_name} WHERE ID = {id}')
        for row in cursor.fetchall():
            cursor.commit()
            return self.model(*list(row))

    def get_by_query(self, query: str) -> List:
        models = []
        cursor = self.connection.cursor()
        cursor.execute(f'SELECT * FROM {self.table_name} WHERE {query}')
        for row in cursor.fetchall():
            models.append(self.model(*list(row)))

        cursor.commit()
        return models

    def create_order(self, client_id: int, service_id: int, start_time: datetime):
        cursor = self.connection.cursor()
        cursor.execute(f'INSERT INTO ClientService (ClientID, ServiceID, StartTime) VALUES (?, ?, ?)', (client_id, service_id, start_time))
        cursor.commit()

    def create_service_image(self, service_id: int, photo_path: str):
        cursor = self.connection.cursor()
        cursor.execute(f'INSERT INTO ServicePhoto (ServiceID, PhotoPath) VALUES (?, ?)', (service_id, photo_path))
        cursor.commit()

    def update_service(self, new_model: ServiceModel):

        cursor = self.connection.cursor()
        query = f'UPDATE {self.table_name} SET Title = ?, Cost = ?, DurationInSeconds = ?, Description = ?, Discount = ?, MainImagePath = ? WHERE ID = ?'
        cursor.execute(query, (
            new_model.title,
            new_model.cost,
            new_model.duration_in_seconds,
            new_model.description,
            new_model.discount,
            new_model.main_image_path,
            new_model.id
        ))
        cursor.commit()

    def delete(self, *, model_id: int):
        cursor = self.connection.cursor()
        cursor.execute(f'DELETE FROM {self.table_name} WHERE id = {model_id}')
        cursor.commit()
