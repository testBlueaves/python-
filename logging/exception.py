import logging
# logging.basicConfig(filename="abc.log",level=logging.INFO,filemode='w')
logging.basicConfig(format='%(asctime)s:%(name)s: %(levelname)s: %(message)s',datefmt = '%d-%m-%Y %I:%M:%S %p',level=logging.INFO)

try:
	x=11
	y=0
	print(x/y)
except ZeroDivisionError as msg:
	print("exception occurs",msg)
	logging.exception(msg)
logging.info("read compltely")