import datetime
from typing import List

from _decimal import Decimal

from database import Database
from models import ServiceModel, ServicePhotoModel, ClientServiceModel


def main():
    db = Database(table_name='ClientService', model=ClientServiceModel)
    records: List[ClientServiceModel] = db.get_all_records(datetime.datetime(2019, 4, 27), datetime.datetime(2019, 9, 10))


if __name__ == '__main__':
    main()
