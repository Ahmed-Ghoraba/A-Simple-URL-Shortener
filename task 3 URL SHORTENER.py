from tkinter import *
import pyshorteners
import tkinter.messagebox as msgbox
import clipboard
def shortner():

    global url
    global short_url
    url = url_holder.get()
    short_url = s.tinyurl.short(url)
    mesg.configure(text=short_url)
    
def copy_to_clipboard():
    short_url = mesg.cget("text")
    clipboard.copy(short_url)
    msgbox.showinfo("Copied", "The shortened URL has been copied to the clipboard.")
###
s = pyshorteners.Shortener()
###TKINTER
urlShortner = Tk()
urlShortner.title('URL Shortner')
urlShortner.geometry('980x560')
urlShortner.config(bg='#CCCCCC')
#----GETTING MAIL----# 
msg = Label(urlShortner, text="Please Enter The URL", justify=LEFT, bg='white', font=("Arial", 16))
msg.place(x=120, y=40)

url_holder = Entry(urlShortner, width=90, font=("Arial", 16), borderwidth=0)
url_holder.place(x=340, y=40)
url_button = Button(urlShortner, text="Shorten My URL", width=16, height=1, font=("Arial", 20), borderwidth=0, bg="#000000", fg="white", command=shortner)
url_button.place(x=550, y=150)

mesg= Label(urlShortner, text = "", font=("Arial", 20))
mesg.place(x=200,y=350)
        
copier = Button(urlShortner , text = "Copy URL", command= copy_to_clipboard)
copier.place(x=230 , y = 400)
urlShortner.mainloop()
