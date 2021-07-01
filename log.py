
'''
This python script is used to write log entries to a log file.
'''

import re
import logging
from logging.handlers import TimedRotatingFileHandler
import os

def setup_logger():
    log_format = "%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s"
    log_level = logging.INFO    
    handler = TimedRotatingFileHandler(os.getcwd()+'\log\log.txt', when="midnight", interval=1)
    handler.setLevel(log_level)
    formatter = logging.Formatter(log_format)
    handler.setFormatter(formatter)

    # add a suffix which you want
    handler.suffix = "%Y%m%d"

    # need to change the extMatch variable to match the suffix for it
    handler.extMatch = re.compile(r"^\d{8}$")

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger
