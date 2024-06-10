import logging

logger = logging.getLogger(__name__)

logger.debug("Loading child_script...")


def child_function():
    logger.debug("Hello from child_function!")
