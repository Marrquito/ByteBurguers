import logging
import psycopg2

from api.requests.itemsOrder import *
from api.responses.itemsOrder import *

from datetime import datetime

logger = logging.getLogger("ByteBurgers")

db_config = {
    "host": "localhost",
    "port": "5532",
    "database": "byte_burgers",
    "user": "byte_burgers",
    "password": "udacaduc123!",
}

class ItemsOrderController:
    def __init__(self):
        logger.debug("ItemsOrder_Service init")

    def create(self, itemsOrder: ItemsOrderRequestModel):
        logger.debug("Create ItemsOrder entry service")
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        try:
            select_query = "SELECT cost FROM menu WHERE id = %s"
            cursor.execute(select_query, (str(itemsOrder.menu_id)))

            price = cursor.fetchone()
            order_total = itemsOrder.qtd * price[0]

            insert_query = "INSERT INTO \"itemsOrdered\" (qtd, total_price, order_id, menu_id) VALUES (%s, %s, %s, %s)"
            data = (itemsOrder.qtd, order_total, itemsOrder.order_id, itemsOrder.menu_id)

            cursor.execute(insert_query, data)

            connection.commit()

        except Exception as e:
            logger.error(f"Error creating itemsOrder entry - {e}")
        
            connection.close()
            
            return False
        
        connection.close()
        
        return True
    
    def read(self, id: int):
        logger.debug("Read ItemsOrder entry service")
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        try:
            select_query = "SELECT * FROM \"itemsOrdered\" WHERE id = %s"
            cursor.execute(select_query, (str(id)))

            result = cursor.fetchone()

            if result is None:
                return None

            itemsOrder = ItemsOrderResponseModel(
                id = result[0],
                qtd = result[1],
                total_price = result[2],
                order_id = result[3],
                menu_id = result[4]
            )

        except Exception as e:
            logger.error(f"Error reading itemsOrder entry - {e}")
        
            connection.close()
            
            return None
        
        connection.close()

        return itemsOrder
    
    def read_all(self, id:int):
        logger.debug("Read all ItemsOrder entry service")

        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        try:
            select_query = "SELECT * FROM \"itemsOrdered\" WHERE order_id = %s"
            cursor.execute(select_query, (str(id)))

            result = cursor.fetchall()

            if result is None:
                return None

            itemsOrder = []

            for item in result:
                itemsOrder.append(
                    ItemsOrderResponseModel(
                        id = item[0],
                        qtd = item[1],
                        total_price = item[2],
                        order_id = item[3],
                        menu_id = item[4]
                    )
                )
        
        except Exception as e:
            logger.error(f"Error reading itemsOrder entry - {e}")
        
            connection.close()
            
            return None
        
        connection.close()

        return itemsOrder
