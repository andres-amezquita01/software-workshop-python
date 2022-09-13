from colorama import init, Fore
from colorama import init, Fore

import datetime as dt
import log_class.logger as lg

init(autoreset=True)

class LoggerConsole(lg.Logger):
    
    def info(self, message, object):
        print(f'{Fore.BLUE}{dt.datetime.now()} [INFO] {message, object}')
    
    def warning(self, message, object):
        print(f'{Fore.YELLOW}{dt.datetime.now()} [WARNING] {message, object}')

    def error(self, message, object):
       print(f'{Fore.RED}{dt.datetime.now()} [ERROR] {message, object}')

    def debug(self, message, object):
        print(f'{Fore.MAGENTA}{dt.datetime.now()} [DEBUG] {message, object}')
