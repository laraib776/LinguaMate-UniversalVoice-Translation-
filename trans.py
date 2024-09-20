# importing requirements
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from googletrans import Translator,LANGUAGES
import ctypes
import os
import pyttsx3

ctypes.windll.shcore.SetProcessDpiAwareness(1)

def change(text="type",src="English",dest="Hindi"):
    trans = Translator()
    text1=text
    src1=src
    dest1=dest
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = sor_txt.get(1.0,END)
    textget = change(text = msg, src=s, dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END, textget) 

engine=pyttsx3.init()

def speaknow():
    text = sor_txt.get(1.0,END)
    gender=comb_gen.get()
    speed=comb_speed.get()
    voices=engine.getProperty('voices')
    
    def setvoice():
        if gender=="Male":
            engine.setProperty("voice",voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty("voice",voices[1].id)
            engine.say(text)
            engine.save_to_file(text,"text.mp3")
            engine.runAndWait()
            
    if text:
        if speed=="Fast":
            engine.setProperty("rate",250)
            setvoice()
        elif speed=="Normal":
            engine.setProperty("rate",150)
            setvoice()
        else:
            engine.setProperty("rate",70)
            setvoice()
            
def download():
    text = sor_txt.get(1.0,END)
    gender=comb_gen.get()
    speed=comb_speed.get()
    voices=engine.getProperty("voices")
    
    def setvoice():
        if gender=="Male":
            engine.setProperty("voice",voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.runAndWait()
        else:
            engine.setProperty("voice",voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,"text.mp3")
            engine.runAndWait()
            
    if text:
        if speed=="Fast":
            engine.setProperty("rate",250)
            setvoice()
        elif speed=="Normal":
            engine.setProperty("rate",150)
            setvoice()
        else:
            engine.setProperty("rate",70)
            setvoice()
   


    
#window geometry and color
root=Tk()
root.title("Translator")
root.geometry("800x600")
root.configure(bg="light blue")
                                    
                                                # LABELS
        
# Translator Label 
lab_txt=Label(root,text="Translator", font=("Time New Roman", 20, "bold"),bg="pink")
lab_txt.place(x=270,y=20,width=250,height=50)

# source label 
lab_txt=Label(root,text="Source Text", font=("Time New Roman", 12, "bold"),fg="Black", bg="light blue")
lab_txt.place(x=20,y=85,width=350,height=20)

# destination label
lab_txt=Label(root,text="Translated Text ", font=("Time New Roman", 12, "bold"),fg="Black", bg="light blue")
lab_txt.place(x=400,y=85,width=350,height=20)

#voice label
lab_txt=Label(root,text="Voice ", font=("Time New Roman", 11, "bold"),bg="light blue")
lab_txt.place(x=25,y=325,width=350,height=30)

#speed label
lab_txt=Label(root,text="Gender", font=("Time New Roman", 11, "bold"),bg="light blue")
lab_txt.place(x=400,y=325,width=350,height=30)

                                                #FRAMES
#Frame for source text for language conversion
frame = Frame(root).pack(side=BOTTOM)
sor_txt=Text(frame,font=("Time New Roman", 15),wrap=WORD)
sor_txt.place(x=25,y=115,height=115,width=350)

#Frame for destination text for language converted
frame = Frame(root).pack(side=BOTTOM)
dest_txt=Text(frame,font=("Time New Roman", 15),wrap=WORD)
dest_txt.place(x=400,y=115,height=115,width=350)

list_txt = list(LANGUAGES.values())

                                              # LANGUAGES COMBOBOX
#drop down list of languages
comb_sor= ttk.Combobox(frame, value=list_txt)
comb_sor.place(x=25,y=235,width=350,height=30)
comb_sor.set("English")

#drop down list of languages (combobox2)
comb_dest= ttk.Combobox(frame, value=list_txt)
comb_dest.place(x=400,y=235,width=350,height=30)
comb_dest.set("language")

# gender combobox
comb_gen=ttk.Combobox(frame, value=["Male","Female"])
comb_gen.place(x=400,y=360,width=350,height=30)
comb_gen.set("Female")

#speed combobox
comb_speed=ttk.Combobox(frame, value=["Fast","Normal","Slow"])
comb_speed.place(x=25,y=360,width=350,height=30)
comb_speed.set("Normal")
                                       #BUTTONS
#button for translation
button_change = Button(frame, text="Translate",relief=RAISED, command=data, bg="pink")
button_change.place(x=325,y=290,width=115,height=28)

# button for speak
button_speak =Button(frame, text="Speak",relief=RAISED, bg="pink", command=speaknow)
button_speak.place(x=25,y=400,width=350,height=28)

#download
button_down = Button(frame, text="Download",relief=RAISED, bg="pink",command=download)
button_down.place(x=400,y=400,width=350,height=28)

root.mainloop()