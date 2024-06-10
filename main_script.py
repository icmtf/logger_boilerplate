import logging, os
import logging.config
import yaml

with open("logging_config.yaml", "r") as file:
    logger_config = yaml.safe_load(file.read())
# Set up logfile name based on "app_name" key. Or else use default name.
app_name = logger_config.get("app_name", "default_app")
log_filename = f"{app_name}.log"
logger_config["handlers"]["file"]["filename"] = log_filename

# Init logger config.
logging.config.dictConfig(logger_config)

# Creating logger instance.
logger_name = os.path.splitext(os.path.basename(__file__))[0]
logger = logging.getLogger(logger_name)

# Importing other modules here would help paprsing lines like:
# logger.debug('Loading child_function')
# If you're not interested then simply import modules in the old fashioned way
# before logger configuraion and init
from child_script import child_function


def main():
    logger.debug("Hey! A Debug log from function here!")


if __name__ == "__main__":
    logger.debug("Testing logs - DEBUG.")
    logger.info("Testing logs - INFO.")
    logger.warning("Testing logs - WARNING.")
    logger.error("Testing logs - ERROR.")
    logger.critical("Testing logs - CRITICAL.")
    main()
    child_function()
