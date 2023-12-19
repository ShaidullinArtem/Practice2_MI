import datetime
from dataclasses import dataclass


@dataclass
class ClientServiceModel:
    id: int
    client_id: int
    service_id: int
    start_time: datetime.time
    comment: str
