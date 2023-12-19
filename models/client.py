import datetime
from dataclasses import dataclass


@dataclass
class ClientModel:
    id: int
    first_name: str
    last_name: str
    patronymic: str
    birthday: str
    registration_date: datetime.datetime
    email: str
    phone: str
    gender_code: str
    photo_path: str
