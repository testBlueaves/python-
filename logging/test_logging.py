import logging
logging.basicConfig(filename='log.txt',level=logging.WARNING,filemode='a')
logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')
