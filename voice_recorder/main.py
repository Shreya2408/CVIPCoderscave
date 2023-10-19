from tkinter import *
from tkinter import messagebox
import sounddevice as sound
from scipy.io.wavfile import write
import time
import wavio as wv
from PIL import Image, ImageTk

root=Tk()
root.geometry("400x500")
root.resizable(False,False)
root.title("Voice recoder")
root.configure(background= "black")

def Record():
    freq=44100
    dur=int(duration.get())
    recording=sound.rec(dur*freq,samplerate=freq,channels=2)
    
    try:
        temp=int(duration.get())
    except:
        print("Please enter the right value")
        
    while temp>0:
        root.update()
        time.sleep(1)
        temp-=1
        
        if (temp==0):
            messagebox.showinfo("Time countdown","Time's Up")
        Label(text=f"{str(temp)}",font="arial",width=4,background="white").place(x=240,y=590)
        
    sound.wait()
    write("Recording.wav",freq,recording)

image_icon = PhotoImage(file="vice.png")
root.iconphoto(False, image_icon)

pic=Image.open("vice.png")
resize = pic.resize((300,225),Image.ANTIALIAS)

npic = ImageTk.PhotoImage(resize)

pic= PhotoImage(file="vice.png")
myimage=Label(image=npic, background="white")
myimage.pack(pady=20)

Label(text="Text Recoder", font="arial 30", background="white", fg="white").pack

duration = StringVar()
entry= Entry(root, textvariable=duration, font=" arial 30", width=15).pack(pady=10)
Label(text="Enter time in secs", font="arial 15",background="black",fg="white").pack()

record=Button(root, font="arial 20",text="record",bg="#111111",fg="white",border=0,command=Record).pack(pady=30)

root.mainloop()