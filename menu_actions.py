from abc import ABC,abstractmethod
class AbstractList(ABC):

    @abstractmethod
    def run(self):
        pass

class Exit(AbstractList):

    def run(self):
        exit()