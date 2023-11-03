import logging
import psycopg2

from api.requests.menu import *

logger = logging.getLogger("ByteBurgers")

db_config = {
    "host": "localhost",
    "port": "5532",
    "database": "byte_burgers",
    "user": "byte_burgers",
    "password": "udacaduc123!",
}

connection = psycopg2.connect(**db_config)

cursor = connection.cursor()

class MenuController:
    def __init__(self):
        logger.debug("Menu_Service init")

    def create(self, menu: MenuRequestModel):
        logger.debug("Create Menu entry service")

        try:
            insert_query = "INSERT INTO menu (name, cost, description, fabrication_place) VALUES (%s, %s, %s, %s)"
            data = (menu.name, menu.cost, menu.description, menu.fabrication_place)

            cursor.execute(insert_query, data)

            connection.commit()

        except Exception as e:
            logger.error(f"Error creating menu entry - {e}")
        
            cursor.close()
            connection.close()
            
            return False
        
        cursor.close()
        connection.close()
        
        return True