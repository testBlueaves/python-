import logging
# creation of looger object and set the logger
logger = logging.getLogger('demologger')
logger.setLevel(logging.DEBUG)

# handler are StreamHandler,FileHandler here we can create obj
fileHandler = logging.FileHandler('fileha.log',mode='a')
#bydefault logger level is handlerlevel
fileHandler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s:%(name)s: %(levelname)s: %(message)s',datefmt = '%d-%m-%Y %I:%M:%S %p')

#add formatter to handler
fileHandler.setFormatter(formatter)

# add handler to logger
logger.addHandler(fileHandler)

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')