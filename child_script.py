import logging

logger = logging.getLogger(__name__)

logger.debug("Loading child_function")


def child_function():
    logger.debug("Hello from child_function!")
