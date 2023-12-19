import datetime
from dataclasses import dataclass


@dataclass
class ManufacturerModel:
    id: int
    name: str
    start_data: datetime.datetime
