from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

class distribute_page():
    
    db = MySQLdb.connect(host="localhost",  user="root", passwd="", db="store")
    gui = Tk()

    def distributeFrom(self,p,h,j,l,o,y):
        #get item_id from item name
        cur2 = self.db.cursor()
        query2="select item_id from fruits where item_name='"+p.get()+"';"
        cur2.execute(query2)
        for row in cur2.fetchall():
            item_id=str(row[0])

        #get user_id from user_name
        cur3 = self.db.cursor()
        query3="select user_id from user where user_name='"+y.get()+"';"
        cur3.execute(query3)
        for row in cur3.fetchall():
            user_id=str(row[0])

            
        cur = self.db.cursor()
        cur5=self.db.cursor()
        query5="select quantity,total_price from stores where item_name='"+p.get()+"';"
        cur5.execute(query5)
        for row in cur5.fetchall():
            quantity=row[0]
            total_price=row[1]
            
        query="insert into supply(date,company_name,user_id,quantity_kg,total_price,item_id) values('"+o.get()+"','"+h.get()+"','"+user_id+"','"+j.get()+"','"+l.get()+"','"+item_id+"'); "
        query4="update stores set quantity='"+str(quantity-int(j.get()))+"' , total_price='"+str(total_price-int(l.get()))+"' where item_id='"+item_id+"';"
        print(query)
        print(query4)
        cur.execute(query)
        cur.execute(query4)
        self.db.commit()

        #added to store message
        t = Label(self.gui ,text="Item Removed From store!!!")
        t.grid(sticky=W,row=27,column = 3,padx=20, pady=40)
        t.config(font=("Courier", 18))
       

    def goToMainMenu(self):
        self.gui.destroy()
        exec(open("main.py").read())
    

        

    def GUI(self):
        self.gui.geometry("800x800")
        self.gui.title("Add To Store")
        large_font = ('Verdana',22)
        #background image
        image =Image.open('C:\\Users\\DELL\\Desktop\\store\\image1.jpg')
        image = image.resize((800, 800), Image.ANTIALIAS)
        photo_image = ImageTk.PhotoImage(image)
        label = Label(self.gui, image = photo_image)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        #topic register
        topic=Label(self.gui,text="Remove")
        topic.grid(sticky=W,row=0,column=5,padx=10, pady=5)
        topic.config(font=("Courier", 44))
        #item name label
        g = Label(self.gui ,text="Item")
        g.grid(sticky=W,row=10,column = 3,padx=20, pady=20)
        g.config(font=("Courier", 22))

        #item name drop down
        optionList = []
        #take  drop down elements from db
        cur = self.db.cursor()
        query="select * from fruits"
        cur.execute(query)
        for row in cur.fetchall():
            optionList.append(row[1])
        
        dropVarChanges=StringVar()
        dropVarChanges.set("Choose Item Name")
        dropMenuChanges = OptionMenu(self.gui ,dropVarChanges,*optionList, )
        dropMenuChanges.grid(column=5,row=10)
        dropMenuChanges.config(font=("Courier", 22))

        #company name label
        #item name label
        g = Label(self.gui ,text="Company")
        g.grid(sticky=W,row=12,column = 3,padx=20, pady=20)
        g.config(font=("Courier", 22))

        #company entry
        h = Entry(self.gui,font=large_font)
        h.grid(sticky=W,row=12,column=5,padx=20, pady=20)
        h.config(font=("Courier", 18))

        #Quantity label
        i = Label(self.gui ,text="Quantity")
        i.grid(sticky=W,row=14,column = 3,padx=20, pady=20)
        i.config(font=("Courier", 22))

        #Quantity entry
        j = Entry(self.gui,font=large_font)
        j.grid(sticky=W,row=14,column=5,padx=20, pady=20)
        j.config(font=("Courier", 18))

        #price label
        k = Label(self.gui ,text="Price")
        k.grid(sticky=W,row=16,column = 3,padx=20, pady=20)
        k.config(font=("Courier", 22))

        #price entry
        l = Entry(self.gui,font=large_font)
        l.grid(sticky=W,row=16,column=5,padx=20, pady=20)
        l.config(font=("Courier", 18))

        #date label
        n = Label(self.gui ,text="Date")
        n.grid(sticky=W,row=18,column = 3,padx=20, pady=20)
        n.config(font=("Courier", 22))

        #date entry
        o = Entry(self.gui,font=large_font)
        o.grid(sticky=W,row=18,column=5,padx=20, pady=20)
        o.config(font=("Courier", 18))

        #User name label
        m = Label(self.gui ,text="Store Keeper")
        m.grid(sticky=W,row=20,column = 3,padx=20, pady=20)
        m.config(font=("Courier", 22))

        #user name from drop down
        optionList1 = []
        #take  drop down elements from db
        cur1 = self.db.cursor()
        query1="select * from user"
        cur1.execute(query1)
        for row in cur1.fetchall():
            optionList1.append(row[1])
        dropVarChanges1=StringVar()
        dropVarChanges1.set("Choose Store Keeper")
        dropMenuChanges1 = OptionMenu(self.gui ,dropVarChanges1,*optionList1, )
        dropMenuChanges1.grid(column=5,row=20)
        dropMenuChanges1.config(font=("Courier", 22))
        
        
        #Button
        c = Button(self.gui, text="Remove",command=lambda:self.distributeFrom(dropVarChanges,h,j,l,o,dropVarChanges1))
        c.grid(sticky=W,row=25,column=7,padx=20, pady=20)
        c.config(font=("Courier", 22))

        #go to main page
        q = Button(self.gui, text="Main Menu",command=lambda:self.goToMainMenu())
        q.grid(sticky=W,row=27,column=5,padx=20, pady=20)
        q.config(font=("Courier", 22))

        
        

        self.gui.mainloop()
    

obj=distribute_page()
obj.GUI()
