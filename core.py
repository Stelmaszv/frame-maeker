import random
import string
from menu_actions import Exit,SetDir,ListDir,Start

class Run:

    dir=''
    movie_dir=''
    photo_dir=''

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