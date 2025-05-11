import logging

logging.basicConfig(level=logging.DEBUG)
# By default the level is Warning

#Log messages of diffrent loglevels
logging.debug("This is a Debug message")
logging.info("This is a Info message")
logging.warning("This is a Warning")
logging.error("This is an Error")
logging.critical("This is CRITICAL")

#debug < info < warning < error < critical