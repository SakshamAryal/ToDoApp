import logging
import os
import sys
from typing import Optional

LOGGING_FORMAT = "[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s"

DebugLevels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
DebugLevelType = str

def get_logger(
        name: Optional[str], level: Optional[DebugLevelType] = 'DEBUG'
) -> logging.Logger:
    logger = logging.getLogger(name=name)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter(LOGGING_FORMAT))
    logger.addHandler(handler)
    return logger