from tkinter import * 
from tkinter import ttk 
from tkinter import messagebox 
import random as rd 
import gspread 
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credential.json',scope)
client = gspread.authorize(creds)
sheets = client.open('login').sheet1
#############
root = Tk()
root.geometry("400x250")
root.title("students platforme")
# 
def login(event):
    loginNav = Toplevel(root) 
    loginNav.title("login :")
    loginNav.geometry("300x230") 
    var1 = StringVar()
    var2 = StringVar()
    def logIn(event):
        infoFromEnties = [var1.get() , var2.get()]
        infoFromSheet = sheets.get_all_values()
        a = -1
        for i in range(1,len(infoFromSheet)) :
            if infoFromSheet[i][1] == infoFromEnties[0] and infoFromEnties[1] == infoFromSheet[i][2] :
                messagebox.showinfo("login info" , "you are login succefully! ")
                break
            if i == len(infoFromSheet) - 1 : 
                a = 3
        if a != -1 :
            messagebox.showinfo("login info" ,"login faild" )
            

        
    Label(loginNav, text = '' ).grid(row = 0 , columnspan = 2)
    l1 = Label(loginNav, text = 'Email : ' )
    l1.grid(row = 1 , column = 0 , padx = 25  )
    e1 = Entry(loginNav, textvariable = var1 )
    e1.grid(row = 1  , column = 1 )
    Label(loginNav, text = '' ).grid(row = 2 , columnspan = 2)
    l2 = Label(loginNav, text = 'Password : ' )
    l2.grid(row = 3 , column = 0 )
    e2 = Entry(loginNav, textvariable = var2)
    e2.grid(row = 3  , column = 1)
    Label(loginNav, text = '' ).grid(row = 4 , columnspan = 2)
    btn = Button(loginNav,text = "login" , width = 5 , height = 1 , font = ('arial' , 8 , 'bold'))
    btn.grid(row = 5 , column = 3 )
    btn.bind("<ButtonPress>", logIn )

def register(event) : 
    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    registerNav = Toplevel(root)
    registerNav.title("register a new user")
    registerNav.geometry("300x230")
    #
    def registation(event):
        data = [var1.get(), var2.get(), var3.get()]
        sheets.insert_row(data,2)
        messagebox.showinfo("registraion info" , "registration done")
        var1.set("")
        var2.set("")
        var3.set("")
    #Label(registerNav, text = '').grid(row = 0 , columnspan = 2)
    l1 = Label(registerNav,text = 'Full name : ' )
    l1.grid(row = 0 , column = 0 , padx = 20 , pady = 5 ) 
    e1 = Entry(registerNav, textvariable  = var1)
    e1.grid(row = 0 , column = 1)
    #
    Label(registerNav, text = '').grid(row = 1 , columnspan = 2)
    #
    l2 = Label(registerNav,text = 'Email : ')
    l2.grid(row = 2 , column = 0 ,  padx = 20 , pady = 5) 
    e2 = Entry(registerNav, textvariable  = var2)
    e2.grid(row = 2 , column = 1)
    #
    Label(registerNav, text = '').grid(row = 3 , columnspan = 2)
    #
    l3 = Label(registerNav,text = 'Password : ')
    l3.grid(row = 4 , column = 0) 
    e3 = Entry(registerNav, textvariable  = var3)
    e3.grid(row = 4 , column = 1)
    #
    Label(registerNav, text = '').grid(row = 5 , columnspan = 2)
    #Label(registerNav, text = '').grid(row = 6 , columnspan = 2)
    #
    btn1 = Button(registerNav,text = "submit" , width = 5 , height = 1 , font = ('arial' , 8 , 'bold'))
    btn1.grid(row = 7 , column = 3 )
    btn1.bind("<ButtonPress>" , registation)



Label(root , text = "").pack()    
Label(root , text = "").pack()    
btn1 = Button(root,text = "login" ,width = 25 , height = 1 , font = ('arial'  , 15 , 'bold') )
btn1.pack()
btn1.bind("<ButtonPress>" , login)
Label(root , text = "").pack()    
btn2 = Button(root,text = "register",width = 25 , height = 1 , font = ('arial', 15 , 'bold' ))
btn2.pack()
btn2.bind("<ButtonPress>" , register)

Label(root , text = "").pack()    



# var1 = StringVar()
# var2 = StringVar()
# def login(event):
#     print("button pressed!")
#     print(var1.get())
#     print(var2.get())

# l1 = Label(root, text = 'Email : ' )
# l1.grid(row = 0 , column = 0  , rowspan = 2)
# e1 = Entry(root, textvariable = var1 )
# e1.grid(row = 0  , column = 1 ,  rowspan = 2 )
# l2 = Label(root, text = 'Password : ' )
# l2.grid(row = 2 , column = 0 )
# e2 = Entry(root, textvariable = var2)
# e2.grid(row = 2  , column = 1)
# btn = Button(root , text = 'login')
# btn.grid(row = 4 , columnspan = 2 )
# btn.bind("<ButtonPress>", login)



root.mainloop()