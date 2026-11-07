import time
timestamp=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
hour=int(input("enter the time in hour:"))

if hour>=0 and hour<12:
    print("good morning")
if hour>=12 and hour<17:
    print("good afternoon")
if hour>=17 and hour<24:
    print("good night")
