# Importing all the necessary libraries to form the alarm clock:
from tkinter import *
from datetime import datetime, timedelta
import time
# from playsound import playsound
import os
from threading import *

root  =  Tk()  # create root window
root.title("Clock with Alarm")
root.maxsize(400,  300)
root.config(bg="skyblue")

def alarm(set_time):
    alarm_set_label(set_time)
    while True:
        time.sleep(1)
        current_time = datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Current Date is:", date, now)
        print(f'Alarm set to: {set_time}')

        if now == set_time:
            alarm_set_label(None)
            print("Time Is Over")
            file = './digital-alarm.mp3'
            # playsound('./digital-alarm.mp3', False)
            os.system("afplay "+file)
            break


def alarm_threading():
    t1 = Thread(target=alarm_time)
    t1.start()


def alarm_time():
    alarm_hour = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(alarm_hour)


def pomodoro_threading():
    t1 = Thread(target=pomodoro_time)
    t1.start()


def pomodoro_time():
    now = datetime.today()
    time_set = now + timedelta(minutes=1)
    alarm(time_set.strftime("%H:%M:%S"))


def time_current():
    current_time = datetime.now()
    current_time = current_time.strftime("%H:%M:%S")
    lbl.config(text=current_time)
    lbl.after(1000, time_current)


def alarm_set_label(time):
    if time is None:
        text_alarm = f'Alarm Not Set Yet --:--:--'
        lbl_Alarm.pack()
        lbl_Alarm.config(text=text_alarm)
    else:
        text_alarm = f'Alarm Set To {time}'
        lbl_Alarm.pack()
        lbl_Alarm.config(text=text_alarm)



frame1 = Frame(root, height=100,  bg='white')
frame1.pack(fill='both',  padx=10,  pady=5,  expand=True)
lbl = Label(frame1, font=("calibri", 40, "bold"), background="black", foreground="white")
lbl.pack()
time_current()

frame2 = Frame(root,  height=50,  bg='grey')
frame2.pack(fill='both',  padx=10,  pady=5,  expand=True)
time_format = Label(frame2, text="Enter time in 24 hour format!", fg="red", bg="black", font=("calibri", 20, "bold"))
time_format.pack()

frame3 = Frame(root,  height=100,  bg='grey')
frame3.pack(fill='both',  padx=10,  pady=5,  expand=True)
addTime = Label(frame3, text="Hour               Min                    Sec  ", font=20)
addTime.pack(fill=BOTH, expand=TRUE)
# The Variables we require to set the alarm(initialization):

hour = StringVar()
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23'
         )
hour.set(hours[0])
hrs = OptionMenu(frame3, hour, *hours)
hrs.pack(side=LEFT, fill=BOTH, expand=TRUE)

min = StringVar()
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59')
min.set(minutes[0])
mins = OptionMenu(frame3, min, *minutes)
mins.pack(side=LEFT, fill=BOTH, expand=TRUE)

sec = StringVar()
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59')
sec.set(seconds[0])
secs = OptionMenu(frame3, sec, *seconds)
secs.pack(side=LEFT, fill=BOTH, expand=TRUE)

frame4 = Frame(root,  height=100,  bg='white')
frame4.pack(fill='both',  padx=10,  pady=5,  expand=True)
submit = Button(frame4, text="Set Alarm", fg="red", width=10, command=alarm_threading).pack(side=LEFT, expand=TRUE)
pomodoro = Button(frame4, text="Set Pomodoro", fg="blue", width=10, command=pomodoro_threading).pack(side=RIGHT, expand=TRUE)

frame5 = Frame(root,  height=100,  bg='white')
frame5.pack(fill='both',  padx=10,  pady=5,  expand=True)
lbl_Alarm = Label(frame5, font=("calibri", 20, "bold"))
alarm_set_label(None)

root.mainloop()