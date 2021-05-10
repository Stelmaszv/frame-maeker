from abc import ABC,abstractmethod
import os.path
class AbstractList(ABC):

    def __init__(self,Run):
        self.Run=Run

    @abstractmethod
    def run(self):
        pass

class Exit(AbstractList):

    def run(self):
        exit()

class SetDir(AbstractList):

    def run(self):
        dir = input('Dir Location : ')
        if os.path.isdir(dir):
            dir=dir+'\\photos'
            if  os.path.isdir(dir) is False:
                os.mkdir(dir)
            self.Run.dir=dir
        else:
            print(dir, 'This is not dir location')
            self.run()