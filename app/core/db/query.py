import MySQLdb
from app.core.db.session import get_session_dict


def query_dict(query = ''):
    """return query as dict"""
    try:
        db_connection = get_session_dict()

        cursor = db_connection.cursor()
        cursor.execute(query)
        # get all records
        records = cursor.fetchall()
        # return records
    except MySQLdb.connections.Error as e :
        cursor.close()
        db_connection.close()
        raise Exception("Error reading data from MySQL table",e)
    except Exception as err :
        raise Exception(f"Error {type(err)} {err}")
    cursor.close()
    db_connection.close()
    return records


def insert_dict(data, table_name):

    columns = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    sql = "INSERT INTO {} ({}) VALUES ({})".format(table_name, columns, values)

    try:
        db_connection = get_session_dict()

        cursor = db_connection.cursor()
        cursor.execute(sql, tuple(data.values()))
        db_connection.commit()

    except MySQLdb.connections.Error as e :
        cursor.close()
        db_connection.close()
        raise Exception("Error reading data from MySQL table",e)
    except Exception as err :
        raise Exception(f"Error {type(err)} {err}")