from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox
from tkcalendar import Calendar, DateEntry
import time
import datetime
from plyer import notification

win = Tk()

def sendnotif(notiftitle,notifmessage):
    notification.notify( ##title and message are necessary
        title=notiftitle,
        timeout=5,
        message=notifmessage,
    )

def show_error(issue):
    messagebox.showerror('Date/Time Error','Set proper'+issue)

def timechecker(notiftime):
    notiftitle=titlebox.get()
    notifmessage=messagebox.get()
    time_object = time.localtime()
    localtime = time.strftime('%H:%M', time_object) #strftime - string format time
    if notiftime==localtime:
        sendnotif(notiftitle, notifmessage)
    else:
        time.sleep(5)
        timechecker(notiftime)


def submit():
    notiftitle=titlebox.get()
    notifmessage=messagebox.get()
    notifdate=datelabel.cget('text')
    notifhour=hourentry.get()
    notifminute=minuteentry.get()
    notiftime=notifhour+':'+notifminute
    timechecker(notiftime)
    
def get_date(cal,win2):
    datelabel.config(text=cal.get_date())
    win2.destroy()

def getdate():
    win2=Tk()
    cal=Calendar(win2,selectmode="day",date_pattern="dd-mm-y")
    cal.pack()
    Button(win2,text='Select date',command=lambda: get_date(cal,win2)).pack()

win.title('Reminder')
#icon=PhotoImage(file='2242300-middle.png')
#win.iconphoto(True, icon)
win.geometry('500x300')
win.config(background='#8b8f8c')

label=Label(win,text='Reminder App',font=('Ink free',24),bg='white', fg='blue',)
label.place(x=160,y=0)

title=Label(win,text='Title to notify:')
title.place(x=50,y=50)
titlebox=Entry(width=50)
titlebox.place(x=130,y=50)

displaymessage=Label(win,text='Display Message:')
displaymessage.place(x=30,y=100)
messagebox=Entry(width=50)
messagebox.place(x=130,y=100)

today_date=time.strftime("%m/%d/%Y")

datelabel=Label(win,text=today_date,bd=1,relief=SUNKEN,bg='white',width=20)
datelabel.place(x=200,y=150)


datebutton=Button(win,text='Set Date',command=getdate)
datebutton.place(x=130,y=148)


hourlabel=Label(win,text='Hour')
hourlabel.place(x=80,y=200)
hourentry=ttk.Spinbox(win, from_=00, to=23, increment=1,width=8)
hourentry.place(x=115,y=200)


minutelabel=Label(win,text='Minute')
minutelabel.place(x=200,y=200)
minuteentry=ttk.Spinbox(win, from_=00, to=59, increment=1,width=8)
minuteentry.place(x=255,y=200)


submit=Button(win,text='Submit',command=submit,font=('Arial',14),bg='blue',fg='white',)
submit.place(x=200,y=250)


win.resizable(0,0)
win.mainloop()
