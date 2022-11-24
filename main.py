# Importing all the necessary libraries to form the alarm clock:
from tkinter import *
from datetime import datetime, timedelta
import time
# from playsound import playsound
import os
from threading import *


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
        lbl_Alarm.config(text=text_alarm)
    else:
        text_alarm = f'    Alarm Set To {time}'
        lbl_Alarm.config(text=text_alarm)


clock = Tk()
clock.title("Alarm Clock - Pomodoro")
clock.geometry("400x300")

lbl = Label(clock, font=("calibri", 40, "bold"), background="black", foreground="white")
lbl.pack()
time_current()

time_format = Label(clock, text="Enter time in 24 hour format!", fg="red", bg="black", font=("calibri", 20, "bold"))
time_format.pack()

addTime = Label(clock, text="Hour    Min    Sec", font=20)
addTime.pack()
# The Variables we require to set the alarm(initialization):
hour = StringVar()
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23'
         )
hour.set(hours[0])
hrs = OptionMenu(clock, hour, *hours)
hrs.place(x=110, y=140)

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
mins = OptionMenu(clock, min, *minutes)
mins.place(x=175, y=140)

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
secs = OptionMenu(clock, sec, *seconds)
secs.place(x=240, y=140)

# To take the time input by user:
submit = Button(clock, text="Set Alarm", fg="red", width=10, command=alarm_threading).place(x=100, y=180)
pomodoro = Button(clock, text="Set Pomodoro", fg="blue", width=10, command=pomodoro_threading).place(x=220, y=180)

lbl_Alarm = Label(clock, font=("calibri", 20, "bold"))
lbl_Alarm.place(x=60, y=230)
alarm_set_label(None)

clock.mainloop()
# Execution of the window.