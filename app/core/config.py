import os
import multiprocessing
import pathlib

from dotenv import dotenv_values

from app.core.utils.logger import get_logger


CONSTANTA_INT  = ['APP_PORT', 'TIMEOUT', 'WORKERS']
CONSTANTA_BOOL = ['ENABLE_THRESHOLD']
BOOL_TRUE      = 'true'


logger = get_logger(__name__)


class AppConfig:
    ENV:str
    DEBUG:bool
    APP_HOST:str
    APP_PORT:str
    TIMEOUT:int
    LOGLEVEL:str
    TIMEOUT:int
    WORKERS:int
    
    ROOT_DIR = str(pathlib.Path(__file__).parent.parent.parent.absolute())

    os.environ['PYTHONPATH'] = os.pathsep.join([ROOT_DIR])
    
    def __init__(self) -> None:
        
        var_config = dotenv_values(".env")
        for key, value in var_config.items():

            if key in CONSTANTA_INT:
                self.__setattr__(key, int(value))

            elif key in CONSTANTA_BOOL:
                if value.lower() == BOOL_TRUE:
                    self.__setattr__(key, True)
                else:
                    self.__setattr__(key, False)

            else:
                self.__setattr__(key, value)
        
        self.ENV = os.getenv('ENV')


config = AppConfig()


class GunicornConfig:

    total_cpu = multiprocessing.cpu_count() * 2 + 1
    workers = total_cpu if total_cpu > 4 else 4
    
    BIND     = f"{config.APP_HOST}: {config.APP_PORT}"
    TIMEOUT  = config.TIMEOUT
    LOGLEVEL = config.LOGLEVEL
    WORKERS  = workers


gunicorn_config = GunicornConfig()

