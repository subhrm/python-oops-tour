import logging
logging.basicConfig(level=logging.DEBUG, filename='app-log.txt', format='[%(asctime)s] %(levelname)s : %(message)s')
logger = logging.getLogger(__name__)

logger.info("Application is starting up...")

logging.debug("# of  records in database now : 3 ")