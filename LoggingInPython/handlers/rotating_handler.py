import logging
from logging.handlers import RotatingFileHandler
import time

# parameters:
# filename - required
# mode - by default 'a'
# maxBytes - Maximum size of log file before rotating occurs
# encoding - if not given system default is used
# delay - used to delay the creation until a write occurs
# backupCount - how many log files to keep

handler = RotatingFileHandler(filename= 'LoggingInPython/handlers/log.out',
                            maxBytes=2048,
                            # delay= True
                            backupCount=5)

logger = logging.getLogger("MyLogger")
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

# now adding content to log.out:

for _ in range(1000):
    statement = f"the time is {str(time.time())}"
    logger.debug(statement)

# note: if number of rotating tiles exceeds the number of backup count,
# then the oldest file will be deleted to create room for newest one.


''' the dealy, will delay the creation until something is logged to the file'''