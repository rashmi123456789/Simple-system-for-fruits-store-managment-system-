from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

class refer_page():
    
    db = MySQLdb.connect(host="localhost",  user="root", passwd="", db="store")
    gui = Tk()

    def goToMainMenu(self):
        self.gui.destroy()
        exec(open("main.py").read())
    
    
    def GUI(self):
        self.gui.geometry("800x800")
        self.gui.title("Refer Stores")
        large_font = ('Verdana',22)
        #background image
        image =Image.open('C:\\Users\\DELL\\Desktop\\store\\image1.jpg')
        image = image.resize((800, 800), Image.ANTIALIAS)
        photo_image = ImageTk.PhotoImage(image)
        label = Label(self.gui, image = photo_image)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        #topic register
        topic=Label(self.gui,text="Stores")
        topic.grid(sticky=W,row=0,column=7,padx=10, pady=5)
        topic.config(font=("Courier", 44))
        #db query
        cur = self.db.cursor()
        query="select * from stores"
        cur.execute(query)
        
        
        Dt=['Item Name','Quantity','Total Price']
        number=cur.rowcount

        for i in range(1):
            for j in range(3):
                n = Label(text=Dt[j], relief=RIDGE)
                n.grid(row=i+4, column=j+5, sticky=NSEW)
                n.config(font=("Courier", 18))
        i=-1
        for row in cur.fetchall():
            i=i+1
            for j in range(2,5):
                m = Label(text=row[j], relief=RIDGE)
                m.grid(row=i+5, column=j+3, sticky=NSEW)
                m.config(font=("Courier", 18))
        #go to main page
        q = Button(self.gui, text="Main Menu",command=lambda:self.goToMainMenu())
        q.grid(sticky=W,row=60,column=10,padx=20, pady=20)
        q.config(font=("Courier", 22))

       
        self.gui.mainloop()
    

obj=refer_page()
obj.GUI()
