import decimal
from dataclasses import dataclass

from models import ClientServiceModel


@dataclass
class ServiceModel:
    id: int
    title: str
    cost: float
    duration_in_seconds: int
    description: str
    discount: decimal.Decimal
    main_image_path: str


@dataclass
class ServiceToClientService:
    service: ServiceModel
    record: ClientServiceModel


