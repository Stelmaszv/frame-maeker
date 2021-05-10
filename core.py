from menu_actions import Exit,SetDir,ListDir

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
                '2': ListDir(self)
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