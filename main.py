import datetime

from _decimal import Decimal

from database import Database
from models import ServiceModel, ServicePhotoModel


def main():
    db = Database(table_name='ServicePhoto', model=ServicePhotoModel)

    print(db.list())


if __name__ == '__main__':
    main()
