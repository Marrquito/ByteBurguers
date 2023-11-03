import logging
import psycopg2

from api.requests.menu import *
from api.responses.menu import *

logger = logging.getLogger("ByteBurgers")

db_config = {
    "host": "localhost",
    "port": "5532",
    "database": "byte_burgers",
    "user": "byte_burgers",
    "password": "udacaduc123!",
}

class MenuController:
    def __init__(self):
        logger.debug("Menu_Service init")

    def create(self, menu: MenuRequestModel):
        logger.debug("Create Menu entry service")
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        try:
            insert_query = "INSERT INTO menu (name, cost, description, fabrication_place) VALUES (%s, %s, %s, %s)"
            data = (menu.name, menu.cost, menu.description, menu.fabrication_place)

            cursor.execute(insert_query, data)

            connection.commit()

        except Exception as e:
            logger.error(f"Error creating menu entry - {e}")
        
            connection.close()
            
            return False
        
        connection.close()
        
        return True
    
    def update(self, id: int, menu: MenuUpdateRequestModel):
        logger.debug("Update Menu entry service")
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        try:
            update_query = "UPDATE menu SET"
            params = []

            if menu.name is not None:
                update_query += " name = %s,"
                params.append(menu.name)
            if menu.description is not None:
                update_query += " description = %s,"
                params.append(menu.description)
            if menu.cost is not None:
                update_query += " cost = %s,"
                params.append(menu.cost)
            if menu.fabrication_place is not None:
                update_query += " fabrication_place = %s,"
                params.append(menu.fabrication_place)

            update_query = update_query.rstrip(',') + " WHERE id = %s;"
            params.append(id)

            cursor.execute(update_query, params)

            connection.commit()

        except Exception as e:
            logger.error(f"Error updating menu entry - {e}")
        
            connection.close()
            
            return False
        
        connection.close()
        
        return True
    
    def read(self, id: int):
        logger.debug("Read Menu entry service")
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        try:
            select_query = "SELECT * FROM menu WHERE id = %s;"
            cursor.execute(select_query, (str(id)))

            menu = cursor.fetchone()

            if menu is None:
                return None

            menu = {
                "id": menu[0],
                "name": menu[1],
                "description": menu[2],
                "cost": menu[3],
                "fabrication_place": menu[4],
            }

            menu = MenuResponseModel(**menu)

        except Exception as e:
            logger.error(f"Error reading menu entry - {e}")
        
            connection.close()
            
            return None
        
        connection.close()
        
        return menu
    
    def delete(self, id: int):
        logger.debug("Delete Menu entry service")
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        try:
            delete_query = "DELETE FROM menu WHERE id = %s;"
            cursor.execute(delete_query, str(id))

            connection.commit()

        except Exception as e:
            logger.error(f"Error deleting menu entry - {e}")
        
            connection.close()
            
            return False
        
        connection.close()
        
        return True