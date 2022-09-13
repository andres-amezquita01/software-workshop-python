import datetime as dt
import log_class.logger as lg

log_file = 'file.log'

class LoggerFile(lg.Logger):
    def info(self, message, object):
        self.__printFile('INFO', message, object)

    def warning(self, message, object):
        self.__printFile('WARNING', message, object)

    def error(self, message, object):
        self.__printFile('ERROR', message, object)
    
    def debug(self, message, object):
        self.__printFile('DEBUG', message, object)
    
    def __printFile(self, nivel, message, object):
        with open(log_file, 'a') as file:
            data = f'{str(dt.datetime.now())} [{nivel}] {message, str(object)}\n'
            file.writelines(data)