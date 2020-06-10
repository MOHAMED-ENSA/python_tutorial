from tkinter import * 
from tkinter import ttk
# 1 
#root = Tk() # creation de la fenaitre
# btn = ttk.Button(root,text ='click me!') # creation de button
# btn.pack() # position de la button
# def btnOnClick():  # event 
#     print("buttom clicked!")
# btn.config(command = btnOnClick) # event on click
# btn.invoke() show message 
#btn.state(["disabled"]) # desactiver l'effet de btn
#btn.state(["!disabled"]) # reactiver le btn
#btn.instate(["disabled"]) # return true if btn is disabled
# 2 
# etr = ttk.Entry(root,width = 30 )
# etr.pack()
# btn1 = ttk.Button(root, text="click me") 
# btn1.pack()
# # afficher le nom tapper par user 
# def printName(): 
#     print(etr.get())
#     etr.delete(0,END)
# btn1.config(command = printName)
# 3
# root = Tk() 
# btn1 = ttk.Button(root , text = " click me  ")
# btn1.pack()
# def btnOnClick(x): 
#     print(f"button clicked!{x}")
# btn1.config(command = lambda : btnOnClick(1))
# 4 : events/listner 
# root = Tk() 
# btn1 = ttk.Button(root , text = " click me  ")
# btn1.pack()
# def btn_click(event) : # on doit obligatoirement ajouter le para event 
#     print("button clicked!")
# btn1.bind('<ButtonPress>', btn_click)

# root.mainloop()


# 4 : style 
# root = Tk() 
# btn1 = ttk.Button(root,text="click me 1")
# btn1.pack()
# btn2 = ttk.Button(root,text="click me 2")
# btn2.pack()
# btn3 = ttk.Button(root,text="click me 3")
# btn3.pack()
# style = ttk.Style() # creation of an object named style
# print(style.theme_use()) # print the actual theme
# print(style.theme_names()) # print all themes
# style.theme_use("classic") # change theme
# style.configure("TButton",foreground = 'black', background = 'skyblue',font = ('arial',24, 'bold')) # change the style of all buttons
# style.configure("Info.TButton" , font = ('arial',24,'italic') ) # create a style new class extends from button
# btn1.configure(style = 'Info.TButton')

# root.mainloop()

# 5 : Grid 
# root = Tk()
# style = ttk.Style() 
# style.theme_use('classic')
# l1 = ttk.Label(root,background = "green" , text = 'Green')
# l1.grid(row = 0 , column = 0) 
# l2 = ttk.Label(root,background = "yellow" , text = 'Yellow')
# l2.grid(row = 0 , column = 1) 
# l3 = ttk.Label(root,background = "blue" , text = 'Blue')
# l3.grid(row = 1 , column = 0,columnspan = 2 , sticky = 'snew' , ipadx = 10 , ipady = 10, padx = 10 , pady = 10)
# l4 = ttk.Label(root,background = "orange" , text = 'Orange')
# l4.grid(row = 0 , column = 2,rowspan = 2 , sticky = 'snew')
# root.rowconfigure(0,weight = 1)
# root.rowconfigure(1,weight = 2)
# root.columnconfigure(0,weight = 1)
# root.columnconfigure(1,weight = 1)
# root.columnconfigure(2,weight = 1)


# root.mainloop()

# 6 : tic tac toy
# from tkinter import messagebox 
# root = Tk() 
# p1 = []
# p2 = [] 
# player = 1 
# root.title('tic tac toy : player 1')
# style = ttk.Style() 
# style.theme_use('classic')
# style.configure("Info.TButton" , backgroud = "red")
# #style.configure("o.TButton" , text = 'o')
# btn1 = ttk.Button(root, text='')
# btn1.grid(row = 0 , column = 0 , sticky = 'snew' , ipadx = 40 , ipady = 40)
# btn1.config(command = lambda :  buClick(1))

# btn2 = ttk.Button(root, text='')
# btn2.grid(row = 0 , column = 1 , sticky = 'snew' , ipadx = 40 , ipady = 40)
# btn2.config(command = lambda :  buClick(2))

# btn3 = ttk.Button(root, text='')
# btn3.grid(row = 0 , column = 2 , sticky = 'snew' , ipadx = 40 , ipady = 40)
# btn3.config(command = lambda :  buClick(3))

# btn4 = ttk.Button(root, text='')
# btn4.grid(row = 1 , column = 0 , sticky = 'snew' , ipadx = 40 , ipady = 40)
# btn4.config(command = lambda :  buClick(4))

# btn5 = ttk.Button(root, text='')
# btn5.grid(row = 1 , column = 1 , sticky = 'snew' , ipadx = 40 , ipady = 40)
# btn5.config(command = lambda :  buClick(5))

# btn6 = ttk.Button(root, text='')
# btn6.grid(row = 1 , column = 2 , sticky = 'snew' , ipadx = 40 , ipady = 40)
# btn6.config(command = lambda :  buClick(6))

# btn7 = ttk.Button(root, text='')
# btn7.grid(row = 2 , column = 0 , sticky = 'snew' , ipadx = 40 , ipady = 40)
# btn7.config(command = lambda :  buClick(7))

# btn8 = ttk.Button(root, text='')
# btn8.grid(row = 2 , column = 1 , sticky = 'snew' , ipadx = 40 , ipady = 40)
# btn8.config(command = lambda :  buClick(8))

# btn9 = ttk.Button(root, text='')
# btn9.grid(row = 2 , column = 2 , sticky = 'snew' , ipadx = 40 , ipady = 40)
# btn9.config(command = lambda :  buClick(9))
# # list contains all buttons : 
# btnList = [btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9]
# def seltLayout(id,text): 
#     btnList[id-1].config(text = text)
# def imp(id) :
#     global p1 
#     global p2 
#     global player 
#     if player == 1 : 
#         seltLayout(id,'x')   # change the text to 'x
#         player = 2 
#         p1.append(id)
#         root.title('tic tac toy player 2')
#         print("p1 = " , p1)
#     elif player == 2 :
#         seltLayout(id ,'O')# change the text to 'o'
#         player = 1 
#         p2.append(id)
#         root.title('tic tac toy player 1')
#         print("p2 = " ,p2)
    

# def winner() : 
#     if (1 in p1 and 2 in p1 and 3 in p1) or (4  in p1 and 4 in p1  and 5 in p1) or (7 in p1 and 8 in p1 and 9 in p1) or (1 in p1 and 4 in p1 and 7 in p1) or (2 in p1 and 5 in p1 and 8 in p1) or (3 in p1 and 6 in p1 and 9 in p1) or (1 in p1 and 5 in p1 and 9 in p1) or (3 in p1 and 5 in p1 and 9 in p1) :
#         messagebox.showinfo(title = 'cong.' , message = 'player 1 won! ')
#         for i in btnList : 
#             i.state(["disabled"])
#     elif (1 in p2 and 2 in p2 and 3 in p2) or (4  in p2 and 4 in p2  and 5 in p2) or (7 in p2 and 8 in p2 and 9 in p2) or (1 in p2 and 4 in p2 and 7 in p2) or (2 in p2 and 5 in p2 and 8 in p2) or (3 in p2 and 6 in p2 and 9 in p2) or (1 in p2 and 5 in p2 and 9 in p2) or (3 in p2 and 5 in p2 and 9 in p2) :
#         messagebox.showinfo(title = 'cong.' , message = 'player 2 won! ')
#         for i in btnList : 
#             i.state(["disabled"])
    

# def buClick(x) : 
#     print(f'x = {x}')
#     imp(x)
#     winner()
# root.mainloop()

# 7 : frame

root = Tk()



root.mainloop()