import os
import sys
import logging
import logging.config
# import dict
from conf import LOGGING_CONFIG_DICT

class CustomLogger(logging.Logger):
    pass

# TODO:
# 1. need debug flag to check format from sys.argv
def logger(namespace,
           output_dir="./output",
           log_file_name="console.log"):

    if not os.path.exists(output_dir):
       os.makedirs(output_dir)

    log_file_path = os.path.join(output_dir, log_file_name)
    LOGGING_CONFIG_DICT["handlers"]["file"]["filename"] = log_file_path
    
    logging.config.dictConfig(LOGGING_CONFIG_DICT)
    logging.setLoggerClass(CustomLogger)

    return logging.getLogger(namespace)

    
    



