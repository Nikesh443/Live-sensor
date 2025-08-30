import logging
import os
import sys
from datetime import datetime

# 1) Create a log filename
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2) Create the folder path "logs"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# 3) Full log file path = folder + filename
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# 4) Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)



