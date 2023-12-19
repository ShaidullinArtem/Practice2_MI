import datetime
from dataclasses import dataclass


@dataclass
class ProductSaleModel:
    id: int
    sale_date: datetime.datetime
    product_id: int
    quantity: int
    client_service_id: int
