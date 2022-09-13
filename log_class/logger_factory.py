from abc import ABC, abstractmethod

class LoggerFactory(ABC):
    
    @abstractmethod
    def get_logger(self, type): pass
