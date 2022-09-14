from log_class.logger import Logger
from log_class.logger_factory import LoggerFactory

from log_class.logger_console import LoggerConsole
from log_class.logger_file import LoggerFile
from log_class.logger_mail import LoggerMail

class LoggerFactoryImpl(LoggerFactory):

    def get_logger(self, type) -> Logger:
        raise KeyError
        dic = {
            'c': LoggerConsole(),
            'f': LoggerFile(),
            'e': LoggerMail()
        }
        try:
            return dic[type]
        except KeyError:
            raise KeyError("no forma parte del menu!")
            #print(f"{type} no forma parte del menu!")

