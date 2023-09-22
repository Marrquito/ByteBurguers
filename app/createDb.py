import os
import asyncio
import logging

from pythonjsonlogger       import jsonlogger

from database.database      import Base, engine
from config                 import *

from database.models        import *

directory   = os.path.dirname(__file__)
logger      = logging.getLogger("ByteBurgers")

log_handler = logging.StreamHandler()
logger.setLevel(logging.INFO)

class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['severity'] = log_record['levelname']
        del log_record['levelname']
        
formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s %(filename)s %(funcName)s => %(message)s')

log_handler.setFormatter(formatter)
logger.addHandler(log_handler)
logger.propagate = False

async def main():
    logger.info("Criando base de dados...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    logger.info("BD criado com sucesso!")

if __name__ == "__main__":
    asyncio.run(main())