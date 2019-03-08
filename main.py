from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

class main_page():  
    gui = Tk()
            
    def refer(self):
        self.gui.destroy()
        exec(open("refer.py").read())

    def addto(self):
        self.gui.destroy()
        exec(open("addto.py").read())

    def distribute(self):
        self.gui.destroy()
        exec(open("distribute.py").read())

    def addNew(self):
        self.gui.destroy()
        exec(open("addNew.py").read())

    def logout(self):
        self.gui.destroy()
      
    
    def GUI(self):
        self.gui.geometry("800x800")
        self.gui.title("Login")
        large_font = ('Verdana',22)
        #background image
        image =Image.open('C:\\Users\\DELL\\Desktop\\store\\image1.jpg')
        image = image.resize((800, 800), Image.ANTIALIAS)
        photo_image = ImageTk.PhotoImage(image)
        label = Label(self.gui, image = photo_image)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        #buttons
        c = Button(self.gui, text="Refer Store",borderwidth=10,command=lambda:self.refer())
        c.grid(sticky=W,row=5,column=2,padx=5, pady=35)
        c.config(font=("Courier", 22))

        d = Button(self.gui, text="Add To Store",borderwidth=10,command=lambda:self.addto())
        d.grid(sticky=W,row=7,column=2,padx=5, pady=35)
        d.config(font=("Courier", 22))

        e = Button(self.gui, text="Remove From Store",borderwidth=10,command=lambda:self.distribute())
        e.grid(sticky=W,row=9,column=2,padx=5, pady=35)
        e.config(font=("Courier", 22))

        f = Button(self.gui, text="Add New Item",borderwidth=10,command=lambda:self.addNew())
        f.grid(sticky=W,row=11,column=2,padx=5, pady=35)
        f.config(font=("Courier", 22))

        g = Button(self.gui, text="Logout",borderwidth=10,command=lambda:self.logout())
        g.grid(sticky=W,row=13,column=0,padx=5, pady=35)
        g.config(font=("Courier", 22))


        self.gui.mainloop()
    

obj=main_page()
obj.GUI()
