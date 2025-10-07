import logging
import os
from datetime import datetime

# Create a folder to store logs
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Name log file by current date and time
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Configure logging format and file location
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] [%(levelname)s] - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)
