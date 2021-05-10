from abc import ABC,abstractmethod
class AbstractList(ABC):

    @abstractmethod
    def run(self):
        pass

class Exit(AbstractList):

    def run(self):
        exit()

class SetDir(AbstractList):

    def run(self):
        print('set dir')