import logging

logger = logging.getLogger('studentLogger')
logger.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler('student.log',mode = 'w')
fileHandler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s',
								datefmt = '%d - %m - %y %I:%M:%S %p')

fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

logger.debug('deug message from student')
logger.info('Info message from student')
logger.warning('Warning message from student')
logger.error('Error message from student')
logger.critical('Critical message from student')


