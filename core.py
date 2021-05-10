class Run:

    dir='rwg'

    def start(self):
        run=True

        while run != False:
            self.set_menu()
            action= input('What do you whant to do ? ')
            if action == '0':
                run = False

            if action == '1':
                print('dir')

    def set_menu(self):
        print('0: exit')
        if len(self.dir)==0:
            print('1:set dir')
        else:
            print('1:start')
            print('2:change dir')
            print('3:list dir')