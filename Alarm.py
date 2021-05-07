from datetime import datetime
from playsound import playsound

alaram_time=input("Enter the time of alarm to be set : HH:MM:SS\n")
alarm_hour=alaram_time[0:2]
alarm_minute=alaram_time[3:5]
alarm_second=alaram_time[6:8]
alarm_period=alaram_time[9:11]

print("Setting Up Alarm:")

while True:
    now=datetime.now()
    current_hour=now.strftime("%I")
    current_minute=now.strftime("%M")
    current_second=now.strftime("%S")
    current_period=now.strftime("%p")
    if(alarm_period==current_period):
        if(alarm_hour==current_hour):
            if(alarm_second==current_second):
                print("Wake Up!")
                playsound('audio.mp3')
                break
    