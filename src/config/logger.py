import sys

from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO")

logger.add("logs/app.log", rotation="500 MB", retention="10 days", level="DEBUG")


def configure_logger():
    return logger
