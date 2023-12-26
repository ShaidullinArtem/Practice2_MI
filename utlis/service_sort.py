from typing import List

from models import ServiceModel
import decimal


def services_price_sort(is_ascending: bool, services: List[ServiceModel]) -> List[ServiceModel]:
    for i in range(len(services)):
        for j in range(len(services)):
            if is_ascending:
                if decimal.Decimal(services[i].cost) < decimal.Decimal(services[j].cost):
                    buf = services[i]
                    services[i] = services[j]
                    services[j] = buf
            else:
                if decimal.Decimal(services[i].cost) > decimal.Decimal(services[j].cost):
                    buf = services[i]
                    services[i] = services[j]
                    services[j] = buf

    return services


def services_discount_sort(down_floor: float, up_floor: float, services: List[ServiceModel]) -> List[ServiceModel]:
    for service in services:
        discount = decimal.Decimal(service.discount)
        if not discount >= down_floor and  not discount <= up_floor:
            services.remove(service)

    return services
