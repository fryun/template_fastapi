import os

from app.core.config import gunicorn_config


bind = gunicorn_config.BIND
timeout = int(gunicorn_config.TIMEOUT)
workers = gunicorn_config.WORKERS
worker_class = "sync"
accesslog = "-"
errorlog = "-"
module = "app.server:app"
log_level = gunicorn_config.LOGLEVEL

    
def on_starting(server):    
     os.environ['GUNICORN_RUN'] = "True"

