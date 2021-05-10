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

    dir=''

    def make_dir(self,dir):
        if os.path.isdir(dir) is False:
            os.mkdir(dir)

    def run(self):
        dir = input('Dir Location : ')
        if os.path.isdir(dir):

            movie_dir= dir+'\\movies'
            photo_dir= dir + '\\photos'
            self.make_dir(movie_dir)
            self.make_dir(photo_dir)
            self.Run.dir=dir
            self.Run.movie_dir = movie_dir
            self.Run.photo_dir = photo_dir
        else:
            print(dir, 'This is not dir location')
            self.run()

    def prepare_dir(self):
        print('list')
        for dir in os.listdir(self.dir):
            print(dir)

