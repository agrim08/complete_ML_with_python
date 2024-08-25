import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S:',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('ArthematicApp')

def add(a,b):
    res = a+b
    logger.debug(f"Adding {a} and {b} = {res}")
    return res

def sub(a,b):
    res = a-b
    logger.debug(f"Subtracting {a} and {b} = {res}")
    return res

def mult(a,b):
    res = a*b
    logger.debug(f"Multiplying {a} and {b} = {res}")
    return res

def divide(a,b):
    try:
        res = a/b
        logger.debug(f"Dividing {a} and {b} = {res}")
        return res
    except:
        logger.error("Zero division error")
        return None
    
add(1,2)
sub(19,8)
mult(5,4)
divide(10,5)
divide(10,0)