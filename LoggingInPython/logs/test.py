from logger import logging

def add(a,b):
    logging.debug("Addition operation is taking place") 
    return a + b

logging.debug("Add function is called")
add(1,2)

