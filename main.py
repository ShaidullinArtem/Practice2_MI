
from database import Database
from models.client import ClientModel


def main():
    db = Database('Client', ClientModel)
    print(db.list())


if __name__ == '__main__':
    main()
