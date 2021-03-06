import random
import string
import os.path
from menu_actions import Exit,SetDir,ListDir,Start,OneMovie
from moviepy.editor import VideoFileClip

class Run:

    dir='D:\project\Frame-Meaker\output'
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
                '3': OneMovie(self),
                '4': Start(self)
            }
            Obj = switcher.get(action, "Invalid data");
            Obj.run()

    def set_menu(self):
        print('\n')
        print('0: exit')
        if len(self.dir)==0:
            print('1:set dir')
        else:
            print('1:change dir ', self.dir)
            print('2:list dir')
            print('3:One movie')
            print('4:start')

        print('\n')

class PhotoMeaker:

    procent_limt = 96
    photo_dir=''

    def __init__(self,Run,file):
        self.file=file
        self.Run=Run
        self.create_dir()

    def create_dir(self):
        if len(self.photo_dir)==0:
            self.photo_dir=self.Run.dir + '\\photos\\'+ self.file
            if os.path.isdir(self.photo_dir) is False:
                os.mkdir(self.photo_dir)

    def set_round_number(self, clip):
        duration = int(clip.duration)
        round_nomber = random.randint(0, int(clip.duration))
        procent = int(round_nomber / duration * 100)
        if procent <= self.procent_limt:
            return round_nomber
        else:
            return self.set_round_number(clip)

    def count_photos(self):
       phots= len(os.listdir(self.photo_dir))
       return self.Run.photos_in_dir-phots

    def make_photo(self):
        clip = VideoFileClip(self.Run.dir + '\\movies\\' + self.file)
        photos=self.count_photos()
        item=0
        for i  in range(0,self.count_photos()):
            frame = self.set_round_number(clip)
            mess = 'creating photos for ' + self.file + ' ' + str(item + 1) + '/' + str(photos)
            frame=self.set_round_number(clip)
            clip.save_frame(self.photo_dir+'\\' + str(StringManipupations.random(20)) + '.png',
                            t=frame)
            print(mess)
            item=item+1

class StringManipupations:

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