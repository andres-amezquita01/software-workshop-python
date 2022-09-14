from log_class.logger import Logger
from log_class.logger_factory import LoggerFactory

from log_class.logger_console import LoggerConsole
from log_class.logger_file import LoggerFile
from log_class.logger_mail import LoggerMail

class LoggerFactoryImpl(LoggerFactory):

    def get_logger(self, type) -> Logger:
        try:
            dic = {
                'c': LoggerConsole(),
                'f': LoggerFile(),
                'e': LoggerMail()
            }
            return dic[type]
        except KeyError:
            raise KeyError("No forma parte del menu!")


