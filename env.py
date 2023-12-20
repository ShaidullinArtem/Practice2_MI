import os
from typing import Final

from dotenv import load_dotenv

load_dotenv()


class Environment:
    DRIVER_NAME: Final = os.environ.get('DRIVER_NAME', '')
    SERVER_NAME: Final = os.environ.get('SERVER_NAME', '')
    DATABASE_NAME: Final = os.environ.get('DATABASE_NAME', '')
    TRUST_CONNECTION: Final = os.environ.get('TRUST_CONNECTION', 'yes')
    PIN_CODE: Final = os.environ.get('PIN_CODE', '')

