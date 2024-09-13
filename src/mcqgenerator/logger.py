""" Script to create logs """

import logging 
import os
from datetime import datetime

# Log file name convention
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y-%H_%M_%S')}.log"

# Create path and log file
log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok=True)

LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILEPATH, 
    level=logging.INFO, 
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s'
)