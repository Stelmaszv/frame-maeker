from abc import ABC,abstractmethod
from moviepy.editor import VideoFileClip
import os.path
import random
movie_ext=('.avi','.mkv','.mp4')

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
            self.prepare_dir()
            self.Run.dir=dir
            self.Run.movie_dir = movie_dir
            self.Run.photo_dir = photo_dir
        else:
            print(dir, 'This is not dir location')
            self.run()

    def prepare_dir(self):
        for dir in os.listdir(self.dir+'\\movies'):
            if dir.endswith(movie_ext):
                movie_dir_location=self.dir+'\\photos\\'+dir
                if os.path.isdir(movie_dir_location) is False:
                    os.mkdir(movie_dir_location)

class ListDir(AbstractList):

    def run(self):
        for dir in os.listdir(self.Run.movie_dir):
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
        from core import stringManipupations
        clip = VideoFileClip('D:\project\Frame-Meaker\output\movies\The X-Files Season 01 Episode 01 - Pilot.avi')
        clip.save_frame('D:\project\Frame-Meaker\output\photos\The X-Files Season 01 Episode 01 - Pilot.avi' + '\\' + str(stringManipupations.random(20)) + '.png',
                        t=self.set_round_number(clip))

