import logging
import psycopg2

from api.requests.table import *
from api.responses.table import *

logger = logging.getLogger("ByteBurgers")

db_config = {
    "host": "localhost",
    "port": "5532",
    "database": "byte_burgers",
    "user": "byte_burgers",
    "password": "udacaduc123!",
}

class TableController:

    def __init__(self):
        logger.debug("Table_Service init")

    def create(self, table: TableRequestModel):
        logger.debug("Create Table service")
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        try:
            
            if table.busy is None:
                table.busy = False

            insert_query = "INSERT INTO \"table\" (qntd_assentos, busy) VALUES (%s, %s)"
            data = (table.qntd_assentos, table.busy)

            cursor.execute(insert_query, data)

            connection.commit()

        except Exception as e:
            logger.error(f"Error creating table - {e}")
        
            connection.close()
            
            return False
        
        connection.close()
        
        return True
    
    def update(self, id: int, table: TableUpdateRequestModel):
        logger.debug("Update Table service")
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        try:
            update_query = "UPDATE \"table\" SET"
            params = []

            if table.qntd_assentos is not None:
                update_query += " qtd_assentos = %s,"
                params.append(table.qntd_assentos)
            if table.busy is not None:
                update_query += " busy = %s,"
                params.append(table.busy)

            update_query = update_query.rstrip(',') + " WHERE id = %s;"
            params.append(id)

            cursor.execute(update_query, params)

            connection.commit()

        except Exception as e:
            logger.error(f"Error updating table - {e}")
            
            connection.close()
        
            return False
             
        connection.close()

        return True

    def delete(self, id: int):
        logger.debug("Delete Table service")
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        try:
            delete_query = "DELETE FROM \"table\" WHERE id = %s;"
            cursor.execute(delete_query, str(id))

            connection.commit()

        except Exception as e:
            logger.error(f"Error deleting table - {e}")
            
            connection.close()
        
            return False
              
        connection.close()

        return True
    
    def read(self, id: int):
        logger.debug("Read Table service")
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        try:
            select_query = "SELECT * FROM \"table\" WHERE id = %s;"
            cursor.execute(select_query, (str(id)))

            table = cursor.fetchone()

            if table is None:
                return None
            
            table = {
                "id": table[0],
                "qntd_assentos": table[1],
                "busy": table[2],
            }

            table = TableResponseModel(**table)

        except Exception as e:
            logger.error(f"Error reading table - {e}")
            
            connection.close()
        
            return False
             
        connection.close()

        return table