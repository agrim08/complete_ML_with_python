import logging

logging.basicConfig(
    filename='app.log', #it will append all logging details and message in a file
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

