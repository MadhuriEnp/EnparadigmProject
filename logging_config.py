from loguru import logger
import sys

def setup_logging():
    logger.remove()  # Remove default logger
    logger.add(sys.stdout, format="{time} - {name} - {level} - {message}", level="INFO")
    logger.add("reports/test_log.log", format="{time} - {name} - {level} - {message}", level="INFO", mode='w')

setup_logging()