import datetime as dt
import log_class.logger as lg
import log_class.log_mail as lm

receiver_email_address = 'andres.amezquita01@uptc.edu.co'

class LoggerMail(lg.Logger):

    def info(self, message, object):
       self.__printMail(receiver_email_address, 'INFO', message, object)

    def warning(self, message, object):
       self.__printMail(receiver_email_address,'WARNING', message, object)

    def error(self, message, object):
        self.__printMail(receiver_email_address, 'ERROR', message, object)
    
    def debug(self, message, object):
        self.__printMail(receiver_email_address, 'DEBUG', message, object)

    def __printMail(self,receiver_email_address, nivel, message, object):
        mail_log = lm.LogMail(receiver_email_address, nivel, message, object)
        mail_log.send_email()