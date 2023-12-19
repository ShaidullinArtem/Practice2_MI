
from database import Database
from models.client import ClientModel


def main():
    db = Database('Client', ClientModel)
    print(db.get_by_query(f'ID = 102'))


if __name__ == '__main__':
    main()
