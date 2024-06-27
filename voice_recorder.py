import sounddevice as sd
from scipy.io.wavfile import write
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askdirectory

add = ""


def file_path():
    global add
    add = askdirectory()


def save_file():
    global add

    time = int(sec.get())
    addr = add + "/" + "deo.wav"
    showinfo(title="Start", message="Recording Starting")
    reco = sd.rec((time * 44100), samplerate=44100, channels=2)
    sd.wait()
    write(addr, 44100, reco)
    showinfo(title="End", message="recording Finished")

def main_window():
    global sec

    win = Tk()
    win.geometry("500x400")
    win.resizable(False, False)
    win.title("SOUND RECORDER")
    win.config(bg="cyan")

    img1 = PhotoImage(file="blackwave.png")
    l1 = Label(win, image=img1)
    l1.place(x=100, y=10, height=150, width=300)

    sec = Entry(win, font=20)
    sec.place(x=150, y=170, height=50, width=200)

    l2 = Label(win, text="Enter time in Seconds", font=("Time New Roman", 20), bg="cyan")
    l2.place(x=100, y=225, height=50, width=300)

    b = Button(win, text="Path", font=("Time New Roman", 20), command=file_path)
    b.place(x=125, y=280, height=30, width=250)

    img2 = PhotoImage(file="mic.png")
    start = Button(win, image=img2, command=save_file)
    start.place(x=225, y=320, height=50, width=50)

    win.mainloop()


main_window()
