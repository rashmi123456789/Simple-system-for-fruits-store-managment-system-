from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

class addNew_page():
    
    db = MySQLdb.connect(host="localhost",  user="root", passwd="", db="store")
    gui = Tk()

    def addNew(self,h,j):
      

            
        cur = self.db.cursor()
        query="insert into fruits(item_name,price_per_kg) values('"+h.get()+"','"+j.get()+"'); "
        cur.execute(query)
        self.db.commit()

        #message
        t = Label(self.gui ,text="Item Added !!!")
        t.grid(sticky=W,row=27,column = 3,padx=20, pady=40)
        t.config(font=("Courier", 18))

    def goToMainMenu(self):
        self.gui.destroy()
        exec(open("main.py").read())
    

        

    def GUI(self):
        self.gui.geometry("800x800")
        self.gui.title("Add New Item")
        large_font = ('Verdana',22)
        #background image
        image =Image.open('C:\\Users\\DELL\\Desktop\\store\\image1.jpg')
        image = image.resize((800, 800), Image.ANTIALIAS)
        photo_image = ImageTk.PhotoImage(image)
        label = Label(self.gui, image = photo_image)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        #topic register
        topic=Label(self.gui,text="Add Items")
        topic.grid(sticky=W,row=0,column=5,padx=10, pady=5)
        topic.config(font=("Courier", 44))
              
        #item name label
        g = Label(self.gui ,text="Item Name")
        g.grid(sticky=W,row=12,column = 3,padx=20, pady=20)
        g.config(font=("Courier", 22))

        #item name entry
        h = Entry(self.gui,font=large_font)
        h.grid(sticky=W,row=12,column=5,padx=20, pady=20)
        h.config(font=("Courier", 18))

        #price per Kg label
        i = Label(self.gui ,text="Price per Kg")
        i.grid(sticky=W,row=14,column = 3,padx=20, pady=20)
        i.config(font=("Courier", 22))

        #price per kg entry
        j = Entry(self.gui,font=large_font)
        j.grid(sticky=W,row=14,column=5,padx=20, pady=20)
        j.config(font=("Courier", 18))

        #Button
        c = Button(self.gui, text="Add",command=lambda:self.addNew(h,j))
        c.grid(sticky=W,row=25,column=7,padx=20, pady=20)
        c.config(font=("Courier", 22))

        #go to main page
        q = Button(self.gui, text="Main Menu",command=lambda:self.goToMainMenu())
        q.grid(sticky=W,row=27,column=5,padx=20, pady=20)
        q.config(font=("Courier", 22))

        
        

        self.gui.mainloop()
    

obj=addNew_page()
obj.GUI()
