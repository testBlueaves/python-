
import logging
import student

logger = logging.getLogger('testlogger')
logger.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler('test.log',mode = 'a')
fileHandler.setLevel(logging.DEBUG)


formatter = logging.Formatter('%(asctime)s-%(name)s-%(message)s',
								datefmt = '%d-%m-%y %I:%M:%S %p')

fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

logger.debug('deug message from test')
logger.info('Info message from test')
logger.warning('Warning message from test')
logger.error('Error message from test')
logger.critical('Critical message from test')
