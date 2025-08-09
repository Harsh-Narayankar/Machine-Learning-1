'''
Any execution or anything that occrs we should log them with massage
'''

import logging
import os
from datetime import datetime

'''
Below will store the log of the perticular step interms of the formate
f"...." (f-string) - is used when you are passing 
'''
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == '__main__':
    logging.info("Cheking whether if working")