#Chirstopher Pullen
# 02.12.2014
# development exercise 1


def details ():
    hours = int(input("please enter the number of hours you wish to be converted"))
    minutes = int(input("please enter the number of minutes"))
    seconds = int(input("please enter the number of seconds"))
    return hours,minutes, seconds

def total (hours, minutes , seconds):
    if hours > 0:
        seconds_hours = (hours*60)*60
    if minutes > 0 :
        seconds_minutes = minutes*60
    total_seconds = seconds_hours + seconds_minutes + seconds
    return total_seconds

def output (total_seconds):
    print (total_seconds)



hours,minutes,seconds = details ()
total_seconds = total (hours,minutes,seconds)
output(total_seconds)
