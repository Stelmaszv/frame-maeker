from menu_actions import Exit,SetDir

class Run:

    dir=''

    def start(self):
        run=True

        while run != False:
            self.set_menu()
            action= input('What do you whant to do ? ')
            switcher = {
                '0': Exit(self),
                '1': SetDir(self)
            }
            Obj = switcher.get(action, "Invalid data");
            Obj.run()

    def set_menu(self):
        print('0: exit')
        if len(self.dir)==0:
            print('1:set dir')
        else:
            print('2:start')
            print('3:change dir ',self.dir)
            print('4:list dir')