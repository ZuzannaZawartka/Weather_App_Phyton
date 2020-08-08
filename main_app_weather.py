from tkinter import *
from PIL import Image , ImageTk
import requests
root = Tk()
def labelPrint(weather):
    name = weather["name"]
    desc = weather["weather"][0]['description']
    temper = weather["main"]['temp']
    return name + "\n\n" + desc + "\n\n" + str(temper) + " "
def getWeather(textbox):
    
    url = "https://api.openweathermap.org/data/2.5/weather"
    key1 = "3f71308adcee47bf88ef55c3660179f8"
    params = {"APPID" : key1 , "q" : textbox , "units" : "metric"}
    x = requests.get(url,params = params)
    weather = x.json()
    print(x.json())
    textbox2['text'] = labelPrint(weather)
    
def buttonowy(textbox):
    print("Wpisales" , str(textbox))

img = ImageTk.PhotoImage(Image.open(r"C:\Users\rafzu\Documents\GitHub\Weather_App\Weather_App_Phyton\tlo.png"))

window  = Canvas(root,width = 700 , height = 400 ).pack()

tlo = Label(root,image= img)

framew_b = LabelFrame(root,bg ="#60b563" )

textb2_frame = LabelFrame(root,bg = "#60b563")

textbox2 = Label(root,bg = "white",anchor = "nw",padx = 20,pady = 10)

textbox = Entry(root)

b = Button(root,text = "Sprawdź" , command =lambda : getWeather(textbox.get()))


tlo.place(relwidth=1,relheight=1)
textb2_frame.place(rely = 0.375,relx= 0.07,relwidth = 0.85,relheight = 0.5)
framew_b.place(relwidth = 0.85,relheight = 0.12,rely = 0.18,relx= 0.07)
textbox.place(relx = 0.1,rely=0.2,relwidth = 0.5,relheight = 0.08)
b.place(relx = 0.69 , rely = 0.2, relwidth = 0.2,relheight = 0.08)
textbox2.place(relx = 0.1,rely=0.4,relwidth = 0.79,relheight = 0.45)


root.mainloop()