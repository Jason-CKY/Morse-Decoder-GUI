from tkinter import *

class Dialogue:

    def create_first_dialog(self):
        self.win = Toplevel()
        self.win.wm_title("Congratulations!")
        background = Label(self.win, bg='black')
        background.pack(fill=BOTH, expand=True)
        Label(background, text="You\'ve decoded the morse code! The next location is hidden in a special location card, try scanning it and see where it takes you."
              , font='None 24 bold', bg='black', fg='white').pack()
        subFrame = Frame(background)
        subFrame.pack(anchor=CENTER)
        Button(self.win, text='Destroy', command=self.win.destroy).pack(in_=subFrame, side=LEFT)
        Button(self.win, text='Destroy some more!', command=self.win.destroy).pack(in_=subFrame, side=LEFT)


'''
test = Test_Windows()
root = Tk()
Button(root, text='activate', command=test.create_first_dialog).pack()
root.mainloop()'''
