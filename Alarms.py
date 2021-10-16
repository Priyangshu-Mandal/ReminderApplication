from plyer import notification
import datetime
import time as t


def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="F:\Python GUI Tkinter Tutorial\Project 2\icon.ico",
        timeout=15
    )


while(True):
    with open("reminders.txt") as f:
        content = f.read()
        reminders = content.split("\n")
        for i, reminder in enumerate(reminders):
            if i != len(reminders) - 1:
                remList = reminder.split(",?/?,! ")
                time = str(datetime.datetime.now())[11:19]
                day = datetime.datetime.now().strftime("%A")
                if remList[3] == "Once" and remList[2] == time:
                    notify(remList[0], remList[1])
                    reminders.remove(reminder)
                    t.sleep(1)
                elif remList[3] == "Daily" and remList[2] == time:
                    notify(remList[0], remList[1])
                    t.sleep(1)
                elif remList[3] == "Mon-Fri" and (day != "Sunday" or day != "Saturday") and remList[2] == time:
                    notify(remList[0], remList[1])
                    t.sleep(1)
                elif remList[3] == "Mon-Sat" and day != "Sunday" and remList[2] == time:
                    notify(remList[0], remList[1])
                    t.sleep(1)

    with open("reminders.txt", "w") as file:
        file.write("")
    with open("reminders.txt", "a") as f:
        for i, reminder in enumerate(reminders):
            if i != len(reminders) - 1:
                f.write(f"{reminder}\n")
