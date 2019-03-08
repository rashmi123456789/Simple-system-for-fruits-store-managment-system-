from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

class login_page():
    
    db = MySQLdb.connect(host="localhost",  user="root", passwd="", db="store")
    gui = Tk()

    def login(self,f,e):
        cur = self.db.cursor()
        query="select password from user where email='"+e.get()+"';"
        cur.execute(query)
        for row in cur.fetchall():
            password= (row[0])
        if f.get()==password :
            i = Label(self.gui ,text="You are logged in")
            i.grid(sticky=W,row=27,column = 3,padx=20, pady=40)
            i.config(font=("Courier", 18))
            self.gui.destroy()
            exec(open("main.py").read())
        else:
            j = Label(self.gui ,text="wrong credentials")
            j.grid(sticky=W,row=27,column = 3,padx=20, pady=40)
            j.config(font=("Courier", 18))
            self.gui.destroy()
            exec(open("login.py").read())
      
        
    

        

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
        #topic login
        topic=Label(self.gui,text="Login")
        topic.grid(sticky=W,row=0,column=5,padx=10, pady=5)
        topic.config(font=("Courier", 44))
        #username label
        a = Label(self.gui ,text="Username")
        a.grid(sticky=W,row=20,column = 3,padx=20, pady=40)
        a.config(font=("Courier", 22))
        #username entry
        e = Entry(self.gui,font=large_font)
        e.grid(sticky=W,row=20,column=5,padx=20, pady=40)
        #password label
        b = Label(self.gui ,text="Password")
        b.grid(sticky=W,row=22,column = 3,padx=20, pady=40)
        b.config(font=("Courier", 22))
        #password entry
        f = Entry(self.gui,show="*",font=large_font)
        f.grid(sticky=W,row=22,column=5,padx=20, pady=40)
        #Button
        c = Button(self.gui, text="Login",command=lambda:self.login(f,e))
        c.grid(sticky=W,row=25,column=7,padx=20, pady=40)
        c.config(font=("Courier", 22))

        self.gui.mainloop()
    

obj=login_page()
obj.GUI()
