from tkinter import *
from pytube import YouTube
from tkinter import messagebox

window = Tk()
window.wm_iconbitmap(r"C:\Users\EtSisTeM\Desktop\Trivia\PythonGUI\yt.ico")
St = StringVar()
window.configure(bg='#D6231E')
window.title("Youtube Video Downloader")
window.geometry("600x500")

r = IntVar()


def get_url():
    if En1.get() == None:
        messagebox.showerror(window, message="Please enter youtube url!")

    elif r.get()==2:

        url = YouTube(str(En1.get()))
        mp4files = url.streams.filter(file_extension='mp4')
        video = mp4files.get_highest_resolution()
        video.download(r"C:\Users\EtSisTeM\Desktop")
        messagebox.showinfo(window, message="Downloaded")

    elif r.get()==1:

        url = YouTube(str(En1.get()))
        mp3 = url.streams.filter(only_audio=True).first()
        mp3.download(r"C:\Users\EtSisTeM\Desktop")
        messagebox.showinfo(window, message="Downloaded")

    else:
        messagebox.showerror(window, message="Please select video format!")
La1 = Label(text = "Youtube Video Downloader", font = "Calibri 20 bold", relief = RIDGE, bg= "#BCAAE8")
En1 = Entry(text = "Enter youtube video download link", textvariable=St,
width=40, bg= "#BCAAE8")

Bu1 =  Button(window, text = "Download", command = get_url, height=2, width=15, font = "Times 10 bold", bg= "#BCAAE8")
Ra1 = Radiobutton(window, text = "mp3", variable = r, value=1).place(relx=0.4, rely = 0.4)
Ra1 = Radiobutton(window, text = "mp4", variable = r, value=2).place(relx=0.54, rely = 0.4)


La1.place(relx = 0.25, rely = 0.2)
En1.place(relx = 0.315, rely = 0.32)
Bu1.place(relx = 0.42, rely = 0.5)

window.mainloop()