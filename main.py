
from database import Database
from models import ServiceModel


def main():
    db = Database(table_name='Service', model=ServiceModel)
    db.delete(model_id=1)
    print(db.get_by_id(id=1))


if __name__ == '__main__':
    main()
