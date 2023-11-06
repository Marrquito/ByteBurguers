import logging
import psycopg2

from api.requests.order import *
from api.responses.order import *
from api.controllers.table import *

from datetime import datetime

logger = logging.getLogger("ByteBurgers")

db_config = {
    "host": "localhost",
    "port": "5532",
    "database": "byte_burgers",
    "user": "byte_burgers",
    "password": "udacaduc123!",
}

class OrderController:
    def __init__(self):
        logger.debug("Order_Service init")

    def create(self, order: OrderRequestModel):
        logger.debug("Create Order entry service")
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        select_query = "SELECT id FROM open_tables WHERE id = %s"
        cursor.execute(select_query, (str(order.table_id)))

        result = cursor.fetchone()

        if result is None:
            return False

        try:
            insert_query = "INSERT INTO \"order\" (user_id, table_id, total, time, payment_method) VALUES (%s, %s, %s, %s, %s)"
            data = (order.user_id, order.table_id, order.total, datetime.now(tz=None) , order.payment_method)

            cursor.execute(insert_query, data)

            TableController().update(order.table_id, TableUpdateRequestModel(busy=True))

            connection.commit()

        except Exception as e:
            logger.error(f"Error creating order entry - {e}")
        
            connection.close()
            
            return False
        
        connection.close()
        
        return True
    
    def read(self, id: int):
        logger.debug("Read Order entry service")
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        try:
            select_query = "SELECT * FROM \"order\" WHERE id = %s"
            cursor.execute(select_query, (str(id)))

            result = cursor.fetchone()

            if result is None:
                return None

            order = {
                "id":result[0],
                "date": result[1],
                "total":result[2],
                "payment_method":result[3],
                "user_id":result[4],
                "table_id":result[5]
            }

            order = OrderResponseModel(**order)

        except Exception as e:
            logger.error(f"Error reading order entry - {e}")
        
            connection.close()
            
            return None
        
        connection.close()
        
        return order
    
    def update(self,id:int, order: OrderRequestModel):
        logger.debug("Update Order entry service")
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        try:
            select_query = "SELECT busy FROM \"table\" WHERE id = %s"
            cursor.execute(select_query, (str(order.table_id)))

            result = cursor.fetchone()

            if result[0] is True:
                return False

            TableController().update(order.table_id, TableUpdateRequestModel(busy=True))

            update_query = "UPDATE \"order\" SET"
            params = []

            if order.date is not None:
                update_query += " time = %s,"
                params.append(order.date)
            if order.total is not None:
                update_query += " total = %s,"
                params.append(order.total)
            if order.payment_method is not None:
                update_query += " payment_method = %s,"
                params.append(order.payment_method)
            if order.user_id is not None:
                update_query += " user_id = %s,"
                params.append(order.user_id)
            if order.table_id is not None:
                update_query += " table_id = %s,"
                params.append(order.table_id)

            update_query = update_query.rstrip(',') + " WHERE id = %s;"
            params.append(id)

            cursor.execute(update_query, params)

            connection.commit()

        except Exception as e:
            logger.error(f"Error updating order entry - {e}")
        
            connection.close()
            
            return False
        
        connection.close()
        
        return True
    
    def delete(self, id: int):
        logger.debug("Delete Order entry service")
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        try:
            delete_query = "DELETE FROM \"order\" WHERE id = %s"
            result = cursor.execute(delete_query, (str(id)))
            
            if result is not None:
                return False
            
            connection.commit()

        except Exception as e:
            logger.error(f"Error deleting order entry - {e}")
        
            connection.close()
            
            return False
        
        connection.close()
        
        return True
    
    def close_order(self, id: int, order: OrderUpdateRequestModel):
        logger.debug("Close Order entry service")
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        try:
            '''select_query = "SELECT * FROM \"itemsOrdered\" WHERE order_id = %s"
            cursor.execute(select_query, (str(id)))
            full_order = cursor.fetchall()

            total = 0
            for item in full_order:
                total += item[2]

            update_query = "UPDATE \"order\" SET time = %s, total =%s, payment_method = %s WHERE id = %s"
            cursor.execute(update_query, (datetime.now(tz=None), total, order.payment_method, str(id)))

            close_order = "SELECT * FROM \"order\" WHERE id = %s"
            cursor.execute(close_order, (str(id)))

            result = cursor.fetchone()

            TableController().update(result[5], TableUpdateRequestModel(busy=False))
 
            if result is None:
                return None
            
            response = OrderResponseModel(
                id = result[0],
                date = result[1],
                total = result[2],
                payment_method = result[3],
                user_id = result[4],
                table_id = result[5]
            )

            connection.commit()'''

            query = "SELECT payment_method FROM \"order\" WHERE id = %s" 
            cursor.execute(query, (str(id)))
            result = cursor.fetchone()

            if result[0] != "not_payed_yet":
                return None 

            cursor.execute("SELECT * FROM close_order(%s,%s,%s)", (str(id), datetime.now(), order.payment_method))

            result = cursor.fetchall()

            response = OrderResponseModel(
                id = result[0][0],
                date = result[0][1],
                total = result[0][2],
                payment_method = result[0][3],
                user_id = result[0][4],
                table_id = result[0][5]
            )

            connection.commit()

        except Exception as e:
            logger.error(f"Error closing order entry - {e}")
        
            connection.close()
            
            return None
        
        connection.close()
        
        return response
    
    def read_client(self, id: int):
        logger.debug("Read Order entry service")
        connection = psycopg2.connect(**db_config)

        try:
            cursor = connection.cursor()
            select_query = "SELECT * FROM \"order\" WHERE user_id = %s"
            cursor.execute(select_query, (str(id)))

            result = cursor.fetchall()

            if result is None:
                return None

            orders = []

            for order in result:
                orders.append(OrderResponseModel(
                    id = order[0],
                    date = order[1],
                    total = order[2],
                    payment_method = order[3],
                    user_id = order[4],
                    table_id = order[5]
                ))

        except Exception as e:
            logger.error(f"Error reading order entry - {e}")
        
            connection.close()
            
            return None
        
        connection.close()

        return orders