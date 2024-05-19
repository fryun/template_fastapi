import logging
import os

from rich.console import Console
from rich.logging import RichHandler

LOG_FORMAT_MSG = "%(message)s"
LOG_FORMAT_PID = "[PID %(process)d] - %(message)s"
LOG_FORMAT_FN  = "[%(funcName)s: %(lineno)d] - %(message)s"

CONSOLE = Console(color_system="256", width=150, style="blue")
HIGHLIGHT = ['success']


class CustomAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        # use my_context from kwargs or the default given on instantiation
        my_context = kwargs.pop('uuid', self.extra['uuid'])
        return '[%s] %s' % (my_context, msg), kwargs
    

def get_logger(module_name):
    gunicorn_run = os.getenv("GUNICORN_RUN", False)
    logger = logging.getLogger(module_name)
    logger.propagate = False

    if gunicorn_run:
        log_path = False
        log_format = LOG_FORMAT_PID
        CONSOLE._width = 250
    else:
        log_path = True
        log_format = LOG_FORMAT_FN

    handler = RichHandler(
        rich_tracebacks=False,
        console=CONSOLE,
        show_path=log_path,
        keywords=HIGHLIGHT
        )

    handler.setFormatter(logging.Formatter(log_format))
    
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    return logger

def behave_logger(module_name):
    gunicorn_run = os.getenv("GUNICORN_RUN", False)
    logger = logging.getLogger(module_name)
    logger.propagate = False

    handler = RichHandler(
        rich_tracebacks=False,
        console=CONSOLE,
        tracebacks_show_locals=False,
        show_path=False,
        keywords=HIGHLIGHT
        )
    
    if gunicorn_run:
        log_format = LOG_FORMAT_PID
    else:
        log_format = LOG_FORMAT_MSG
    
    handler.setFormatter(logging.Formatter(log_format))
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    return logger




