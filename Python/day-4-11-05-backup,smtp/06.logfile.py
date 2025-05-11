import logging

logging.basicConfig(
    filename='app.log',
    filemode='a',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.debug('Debugging info')
logging.info('processing started')
logging.warning('something is wrong')
logging.error('data process failed')
logging.critical('system crash..!')
