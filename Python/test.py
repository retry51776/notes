import logging

def get_logger():
    logger = logging.getLogger(__name__)
    print(f'got logger from {__name__}')
    return logger

print('Proof of codes always ran when import')

def another_test(a=get_logger()):
    print('another_test')