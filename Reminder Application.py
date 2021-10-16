import tkinter.messagebox
from tkinter import *

root = Tk()
root.geometry("640x360")
root.wm_iconbitmap("appointment_reminders.ico")
root.title("Reminder")


def saveRem():
    with open("reminders.txt", "a") as f:
        f.write(f"{titleValue.get()},?/?,! {descriptionValue.get()},?/?,! {timeValue.get()},?/?,! {var.get()}\n")
        tkinter.messagebox.showinfo("Note", "Please run the Alarms.py file with pythonw command to activate the reminder")


Label(text="Reminder Title", font=("comicsansms", 13), padx=15).grid(row=1, column=2)
Label(text="Description", font=("comicsansms", 13), padx=15).grid(row=2, column=2)
Label(text="Time (HH:mm:ss)", font=("comicsansms", 13), padx=15).grid(row=3, column=2)
Label(text="Frequency", font=("comicsansms", 13), padx=15).grid(row=4, column=2)

titleValue = StringVar()
descriptionValue = StringVar()
timeValue = StringVar()

Entry(root, textvariable=titleValue).grid(row=1, column=3)
Entry(root, textvariable=descriptionValue).grid(row=2, column=3)
Entry(root, textvariable=timeValue).grid(row=3, column=3)

frequencyList = ["Once", "Daily", "Mon-Fri", "Mon-Sat"]
var = StringVar()
var.set(None)

i = 4
for frequency in frequencyList:
    Radiobutton(root, text=frequency, value=frequency, variable=var, font="comicsansms 12", justify=LEFT).grid(row=i, column=3)
    i += 1

Button(text="Save Reminder", font=("comicsansms", 13), borderwidth=4, relief=RAISED, command=saveRem, pady=5).grid(row=8, column=3, pady=15)

root.mainloop()
