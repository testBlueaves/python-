import logging

logger = logging.gotLogger('studentLogger')
logger.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler('student.log',mode = 'w')
fileHandler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s',datefmt = '%d - %m - %y %I:%M:%S %p)

