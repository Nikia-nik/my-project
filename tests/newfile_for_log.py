import logging
logger = logging.getLogger("Log Test")

def do_something() -> None:
    logger:info("Doing something...")


logging.basicConfig(filename='myapp.log', level=logging.INFO , format ="%(asctime)s %(levelname)s %(name)s %(message)s")
logger.info('Started')
do_something()
logger.info('Finished')
'''python *name file* 
is how you run your file in cmd

%(asctime)s %(levelname)s %(name)s %(message)s
adds the time'''
