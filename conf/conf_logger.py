import sys

# dict based logging configuration
# https://docs.python.org/3/whatsnew/2.7.html#pep-391-dictionary-based-configuration-for-logging
LOGGING_CONFIG_DICT = {
    'version': 1,    # Configuration schema in use; must be 1 for now
    'filters': {},
    'formatters': {
        'default': {
            'format': '[%(asctime)s %(name)s %(levelname)s] %(message)s'
        },
        'debug': {
            # https://docs.python.org/3/library/logging.html#logrecord-attributes
            'format': '[%(asctime)s %(name)s \
{%(funcName)s::%(filename)s::%(lineno)d} %(levelname)s] \
%(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'default',
            'level': 'INFO'
            },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'console.log',
            'encoding': 'utf8',
            'formatter': 'debug',
            'level': 'DEBUG'
            }
    },
    # Specify all the subordinate loggers
    'loggers': {},
    # Specify properties of the root logger
    'root': {
        'level': 'INFO',
        # direct log to both console and file handler
        'handlers': ['console', 'file']
    }
}
# TODO:
# 1. let loggers key to empty, check fileconfig format
# 2. config root is enough?
# 3. singleton? if call dictconfig multiple times?