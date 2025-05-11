import logging

#With Logger name
logger=logging.getLogger("sonam_soni")

logging.basicConfig(level=logging.INFO)
# By default the level is Warning

#Log messages of diffrent loglevels
logger.debug("This is a Debug message")
logger.info("This is a Info message")
logger.warning("This is a Warning")
logger.error("This is an Error")
logger.critical("This is CRITICAL")

#debug < info < warning < error < critical