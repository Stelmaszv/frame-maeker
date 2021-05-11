import os.path
import random
from abc import ABC,abstractmethod
movie_ext=('.avi','.mkv','.mp4','.wmv')

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
            self.dir=dir
            movie_dir= dir+'\\movies'
            photo_dir= dir + '\\photos'
            self.make_dir(movie_dir)
            self.make_dir(photo_dir)
            self.Run.dir=dir
        else:
            print(dir, 'This is not dir location')
            self.run()

class ListDir(AbstractList):

    def run(self):
        for dir in os.listdir(self.Run.dir+'\\movies'):
            if dir.endswith(movie_ext):
                print(dir)

class Start(AbstractList):

    procent_limt = 96

    def set_round_number(self, clip):
        duration = int(clip.duration)
        round_nomber = random.randint(0, int(clip.duration))
        procent = int(round_nomber / duration * 100)
        if procent <= self.procent_limt:
            return round_nomber
        else:
            return self.set_round_number(clip)

    def run(self):
        from core import PhotoMeaker
        counter=1
        print('\n')
        print('Adding photos to movies')
        print('\n')
        for dir in os.listdir(self.Run.dir+'\\movies'):
            if dir.endswith(movie_ext):
                cunter_str = str(counter) + '/' + str(len(os.listdir(self.Run.dir + '\\movies')))
                print('Movie - ' + dir + ' ' + cunter_str)
                PhotoMeaker(self.Run,dir).make_photo()
                counter=counter+1
        print('\n')
        print('Adding photos to movies End !')
        print('\n')

class OneMovie(AbstractList):

    def run(self):
        from core import PhotoMeaker
        file = input('Movie Location : ')
        if file in os.listdir(self.Run.dir+'\\movies'):
            if file.endswith(movie_ext):
                print('\n')
                print('Adding photos to movies')
                print('\n')
                cunter_str = str(1) + '/' + str(1)
                print('Movie - ' + file + ' ' + cunter_str)
                PhotoMeaker(self.Run,file).make_photo()
                print('\n')
                print('Adding photos to movies End !')
                print('\n')
            else:
                print(dir, 'This ext is not allowed')
                self.run()
        else:
            print(dir, 'This is not dir location')
            self.run()

