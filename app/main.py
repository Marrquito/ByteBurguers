import logging
import os

from logging.handlers   import TimedRotatingFileHandler
from pythonjsonlogger   import jsonlogger
from fastapi            import FastAPI

from config             import *

directory   = os.path.dirname(__file__)
logger      = logging.getLogger("ByteBurgers")

#Configure log system:
if PRINT_LOG == "terminal":
    log_handler = logging.StreamHandler()
    logger.setLevel(logging.INFO)

    class CustomJsonFormatter(jsonlogger.JsonFormatter):
        def add_fields(self, log_record, record, message_dict):
            super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
            log_record['severity'] = log_record['levelname']
            del log_record['levelname']

    # formatter = CustomJsonFormatter('''{%(asctime)s , %(levelname)s,  %(funcName)s,  %(message)s, %(module)s}''')
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s %(filename)s %(funcName)s => %(message)s')

    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)
    logger.propagate = False
else:
    logger.setLevel(logging.INFO)
    formatter      = logging.Formatter(fmt='%(asctime)s %(levelname)s %(filename)s %(funcName)s => %(message)s')
    handler        = TimedRotatingFileHandler(os.path.join(directory, "logs", "ByteBurgers"), when="midnight", interval=1)
    handler.suffix = "%Y-%m-%d.log"
    handler.setFormatter(formatter)
    logger.addHandler(handler)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}