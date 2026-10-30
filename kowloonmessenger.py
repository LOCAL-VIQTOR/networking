# LedgerAnalyst.__main__

# IMPORTS
from tkinter import Tk, Menu, Label
import argparse

# CONSTANTS


# FUNCTIONS
def printholder(): print('placeholder')

# CLASSES
class LedgerAnalystInstance():
    def __init__(self,args):
        self.args = args
        self.root = Tk()
        self.CURRENT_SCREEN = 'Home'
        self.home_label = Label(self.root,text='Kowloon',font='Helvetica 48')
        self.WIDGETS = [self.home_label]
        
    def setup_window(self):
        self.root.geometry('400x400')
        self.root.config(background='gray')
        self.root.title('Kowloon')
        self.home_label.place(relx=0.5,rely=0.5,anchor='s')
        
        # Menubar
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        
        # M1FCU Login
        # Records
        records_menu = Menu(menubar, tearoff=0)
        records_menu.add_command(label='Open Records Folder', command=printholder)
        records_menu.add_command(label='Process Records Updates', command=printholder)
        
        # Add Items to Main Menubar
        menubar.add_command(label='Home',command=printholder) # add to open up login
        menubar.add_cascade(label='Messages',menu=records_menu)
        menubar.add_command(label='Contacts',command=lambda: self.change_screen('Edit'))
        menubar.add_command(label='Settings',command=lambda: self.change_screen('Display'))
        menubar.add_command(label='About',command=lambda:self.quit())
        
    def change_screen(self,screen):
        self.CURRENT_SCREEN = screen
        for w in self.WIDGETS: w.place_forget()
        
    def run(self):
        self.setup_window()
        self.root.mainloop()
    
    def quit(self): self.root.destroy()
    
# INSTANCES

# MAIN
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='python3.14 -m LedgerAnalyst',
        description='Personal Ledger Analyst by Calvin Lowe (2026)',
        epilog='Pressing enter on the attached terminal page will close the program.')
    
    parser.add_argument('-s','--sample',help='sample instruction')
    
    args = parser.parse_args()
    lai = LedgerAnalystInstance(args)
    lai.run()
    input('Press Enter to Close the Program from this terminal window.')
