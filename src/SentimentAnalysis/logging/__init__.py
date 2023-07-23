import sys
import logging
from pathlib import Path
from logging.handlers import RotatingFileHandler

log_dir = "logs"
Path(log_dir).mkdir(parents=True, exist_ok=True)

# Configure logger
logging_format = "[%(asctime)s: %(levelname)s: %(module)s] %(message)s"
log_file = Path(log_dir) / "running_logs.log"

logger = logging.getLogger("Sentiment Analysis")
logger.setLevel(logging.INFO)

# Create file handler with rotating capability
file_handler = RotatingFileHandler(log_file, maxBytes=1000000, backupCount=5)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter(logging_format))

# Create console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter(logging_format))

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Test the logger
logger.info("This is an information message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
