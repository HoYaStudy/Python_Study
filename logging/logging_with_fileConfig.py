import logging
import logging.config

logging.config.fileConfig(fname="logging.conf", disable_existing_loggers=False)

logger = logging.getLogger(__name__)
logger.debug("This is debug logging")
