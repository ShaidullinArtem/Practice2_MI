import datetime

from database import Database
from models import ServiceModel


def main():
    db = Database(table_name='Service', model=ServiceModel)
    db.create_order(101, 4, datetime.datetime.utcnow())


if __name__ == '__main__':
    main()
