import MySQLdb
from MySQLdb.connections import Connection

from app.core.config import config


def get_session() -> Connection:
    try:
        db_connection = MySQLdb.connect(host=config.DB_HOST,
                                        port = int(config.DB_PORT),
                                        database=config.DB_NAME,
                                        user=config.DB_USER,
                                        password=config.DB_PASSWORD
                                    )
        return db_connection
    
    except Exception as e :
        raise Exception(f"Cant connect to mysql database")


def get_session_dict() -> Connection:
    try:
        db_connection = MySQLdb.connect(host=config.DB_HOST,
                                        port = int(config.DB_PORT),
                                        database=config.DB_NAME,
                                        user=config.DB_USER,
                                        password=config.DB_PASSWORD,
                                        cursorclass=MySQLdb.cursors.DictCursor,
                                        connect_timeout=int(config.DB_TIMEOUT)
                                    )
        return db_connection
    
    except Exception as e :
        raise Exception(f"Cant connect to mysql database")