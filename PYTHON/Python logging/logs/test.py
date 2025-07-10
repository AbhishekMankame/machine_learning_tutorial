from logs import logging

def add(a,b):
    logging.debug("The additional operation is taking place")
    return a+b

logging.debug("The addition function is called")
add(10,15)