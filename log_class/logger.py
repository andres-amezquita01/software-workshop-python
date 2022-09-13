from abc import ABC, abstractmethod

class Logger(ABC):

    @abstractmethod
    def info(self, message, object): pass

    @abstractmethod
    def warning(self, message, object): pass

    @abstractmethod
    def error(self, message, object): pass

    @abstractmethod
    def debug(self, message, object): pass
