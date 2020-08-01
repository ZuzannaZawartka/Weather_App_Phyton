from tkinter import *
from PIL import Image , ImageTk
import requests
root = Tk()
def buttonowy(textbox):
    print("Wpisales" , str(textbox))

img = ImageTk.PhotoImage(Image.open(r"C:\Users\rafzu\Documents\GitHub\Weather_App\Weather_App_Phyton\tlo.png"))
window  = Canvas(root,width = 700 , height = 400 ).pack()
tlo = Label(root,image= img)

framew_b = LabelFrame(root,bg ="#60b563" )

textbox = Entry(root)

b = Button(root,text = "Sprawdź" , command =lambda : buttonowy(textbox.get()))

label = Label
tlo.place(relwidth=1,relheight=1)
framew_b.place(relwidth = 0.85,relheight = 0.12,rely = 0.18,relx= 0.07)
textbox.place(relx = 0.1,rely=0.2,relwidth = 0.5,relheight = 0.08)
b.place(relx = 0.69 , rely = 0.2, relwidth = 0.2,relheight = 0.08)

root.mainloop()