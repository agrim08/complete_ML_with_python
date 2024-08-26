import logging

''' it is a good practise to follow SPR(single responsibility principle)'''

my_formatter =  logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def file_logger() -> logging.FileHandler:
    # Add file handler:
    file_logger = logging.FileHandler('LoggingInPython/mini_program_handler/log.out')
    file_logger.setLevel(logging.DEBUG) #this will store all debug messages
    file_logger.setFormatter(my_formatter)
    return file_logger

def console_logger() -> logging.StreamHandler:
    # Add console handler
    console_logger = logging.StreamHandler()
    console_logger.setLevel(logging.INFO)
    console_logger.setFormatter(my_formatter)
    return console_logger


def my_logger() -> logging.Logger:
    logger = logging.getLogger("MyLogger")
    logger.setLevel(level=logging.DEBUG)
    #Add hanlder to loggers
    logger.addHandler(file_logger())
    logger.addHandler(console_logger())
    return logger

logger = my_logger() 