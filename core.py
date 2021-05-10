class Run:
    def start(self):
        run=True

        while run != False:
            action= input('What do you whant to do ? ')
            if action == '0':
                run = False