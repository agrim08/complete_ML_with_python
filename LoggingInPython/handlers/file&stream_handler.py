import logging

logger = logging.getLogger("MyLogger")
logger.setLevel(level=logging.DEBUG)

# Add file handler:
file_logger = logging.FileHandler('LoggingInPython/handlers/log.out')
file_logger.setLevel(logging.DEBUG) #this will store all debug messages

# Add console handler
console_logger = logging.StreamHandler()
console_logger.setLevel(logging.INFO)

#apllying two handlers and formatting
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_logger.setFormatter(formatter)
console_logger.setFormatter(formatter)

#Add hanlder to loggers
logger.addHandler(file_logger)
logger.addHandler(console_logger)

#logging some messages
def my_func():
    logger.info("This is info message") #only this will be logged to console
    logger.debug("This is debug message") #but this will log all messages to log.out

my_func()    