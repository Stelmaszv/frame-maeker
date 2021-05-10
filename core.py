import random
import string
import os.path
from menu_actions import Exit,SetDir,ListDir,Start
from moviepy.editor import VideoFileClip

class Run:

    dir=''
    movie_dir=''
    photo_dir=''
    photos_in_dir=20

    def start(self):
        run=True

        while run != False:
            self.set_menu()
            action= input('What do you whant to do ? ')
            switcher = {
                '0': Exit(self),
                '1': SetDir(self),
                '2': ListDir(self),
                '3': Start(self)
            }
            Obj = switcher.get(action, "Invalid data");
            Obj.run()

    def set_menu(self):
        print('0: exit')
        if len(self.dir)==0:
            print('1:set dir')
        else:
            print('1:change dir ', self.dir)
            print('2:list dir')
            print('3:start')

class PhotoMeaker:

    procent_limt = 96

    def __init__(self,Run,file):
        self.file=file
        self.Run=Run

    def set_round_number(self, clip):
        duration = int(clip.duration)
        round_nomber = random.randint(0, int(clip.duration))
        procent = int(round_nomber / duration * 100)
        if procent <= self.procent_limt:
            return round_nomber
        else:
            return self.set_round_number(clip)

    def count_photos(self):
       phots= len(os.listdir(self.Run.dir + '\\movies'))
       print(self.Run.photos_in_dir-phots)
       return self.Run.photos_in_dir-phots

    def make_photo(self):
        for i  in range(0,self.count_photos()):
            clip = VideoFileClip('D:\project\Frame-Meaker\output\movies\The X-Files Season 01 Episode 01 - Pilot.avi')
            frame=self.set_round_number(clip)
            clip.save_frame('D:\project\Frame-Meaker\output\photos\The X-Files Season 01 Episode 01 - Pilot.avi' + '\\' + str(frame) + '.png',
                            t=frame)

class stringManipupations:

    @staticmethod
    def short(string,limit) ->str:
        new=''
        if len(string)>limit:
            for letter in range(len(string)):
                if letter<limit:
                    new=new+str(string[letter])
            new = new+' ...'
        else:
            new = string
        return new

    @staticmethod
    def array_to_string(array)->str :
        string=''
        el=1
        for item in array:
            string=string+str(item.name)
            if el<len(array):
                string=string+str(', ')
                if el % 5==0:
                    string = string + str('<br>')
            el=el+1;
        return str(string)

    @staticmethod
    def random(length) ->str :
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str