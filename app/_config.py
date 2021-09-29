from dotenv import ( load_dotenv, find_dotenv )
from os import getenv

class Config: 
    """
    Data class. Retrieves cconfiguration variables from environment
    """
    load_dotenv(find_dotenv())

    DEBUG = getenv('API_DEBUG') == "true"
    API_HOST = getenv('API_HOST')
    API_PORT = getenv('API_PORT')

    DB_HOST=getenv('DB_HOST')
    DB_USER=getenv('DB_USER')
    DB_PASSWORD=getenv('DB_PASSWORD')
    DB_NAME=getenv('DB_NAME')

    SIGNATURE=getenv('SIGNATURE')
    TOKEN=getenv('TOKEN')
    NO_ROLE_TOKEN=getenv('NO_ROLE_TOKEN')
    VALID_USER=getenv('VALID_USER')
    VALID_PASSWORD=getenv('VALID_PASSWORD')