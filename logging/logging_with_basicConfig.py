import logging

# To Console (Default Logger) ##################################################
logging.basicConfig(level=logging.DEBUG)

logging.critical("This is a critical logging")
logging.error("This is a error logging")
logging.warning("This is a warning logging")
logging.info("This is a info logging")
logging.debug("This is a debug logging")

# To Console (Custom Logger) ###################################################
# handler = logging.StreamHandler()
# handler.setLevel(logging.DEBUG)
# handler.setFormatter(
#     logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# )

# logger = logging.getLogger("hLogger")
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# logger.addHandler(handler)

# logger.critical("This is a critical logging")
# logger.error("This is a error logging")
# logger.warning("This is a warning logging")
# logger.info("This is a info logging")
# logger.debug("This is a debug logging")


# To File ######################################################################
# logging.basicConfig(
#     filename="logging.log",
#     filemode="w",
#     format="%(name)s - %(levelname)s - %(message)s",
#     level=logging.DEBUG,
#     encoding="utf-8",
# )

# logging.critical("This is a critical logging")
# logging.error("This is a error logging")
# logging.warning("This is a warning logging")
# logging.info("This is a info logging")
# logging.debug("This is a debug logging")
