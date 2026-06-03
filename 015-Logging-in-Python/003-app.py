import os
import logging

file_name = '003-app.log'
absolute_path = os.path.abspath('015-Logging-in-Python')
log_full_path = os.path.join(absolute_path,file_name)
print(log_full_path)


# logging setting
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s -%(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    force=True,

    # for file name
    handlers=[
        logging.FileHandler(log_full_path),
        # responsible for inputting all logs inside the the particular .log file
        logging.StreamHandler()
    ]
)


logger= logging.getLogger('Arithmetic_APP')

def add(a,b):
    result = a+b
    logger.debug(f"Adding {a}+{b}: {result}")

    return result

def subtract(a,b):
    result = a-b
    logger.debug(f"subtracting {a}-{b}: {result}")

    return result

def multiply(a,b):
    result = a*b
    logger.debug(f"multiplying {a}*{b}: {result}")

    return result

def divide(a,b):
    try:
        result = a/b
        logger.debug(f"dividing {a}*{b}: {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None




add(14,20)
subtract(20,14)
multiply(20,5)
divide(20,5)

divide(20,0)

