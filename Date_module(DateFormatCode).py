import datetime
from datetime import date
import calendar


def checkFormatCodeVersion(code):

    if ord(code[1]) in range(97,123):
        return True     #If code is short version

    return False     #If code is Full Version

def getDay(code,year,month,day):

    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"] 
    dayNumber=calendar.weekday(year,month,day)

    if checkFormatCodeVersion(code):
        return days[dayNumber][:3]  #Return short version day

    return days[dayNumber]  #Return full version day

def getWeekDayNumber(year,month,day):

    day=getDay("%A",year,month,day)
    days={"Sunday":0,"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6}
    
    return str(days[day])    #Return day number


def getMonthName(code,month):

    Month=['January','February','March','April','May','June','July','August','September','October','November','December']

    if checkFormatCodeVersion(code):
        return Month[month-1][:3]   #Return short version month

    return Month[month-1]   #Return full version month

def getYear(code,year):

    if checkFormatCodeVersion(code):
        return str(year)[2:]    #Return short version year

    return str(year)     #Return full version year


def getDayMonthYear(Date):

    Date=str(Date)[:11]
    year,month,day=map(int,Date.split('-'))     #split date by '-' and convert str into int

    return year,month,day   #Return tuple of year,month and day
    
#  %H :
def getCurrentHour24(Date):
    return str(Date.hour).zfill(2)

# %I :
def getCurrentHour12(Date):
    hour= Date.hour

    if(hour>12):
        h=hour-12
        return str(h).zfill(2)
    else:
        return str(hour).zfill(2)   

# %p:
def getAMorPM(Date):
    hour= Date.hour

    if (hour>=12):
        return "PM"
    else:
        return "AM"

# %M :
def getCurrentMinute(Date):
    minute= Date.minute
    return str(minute).zfill(2)

# %S :
def getCurrentSec(Date):
    sec= Date.second
    return str(sec).zfill(2)

# $f :
def getCurrentMicrosec(Date):
    msec= Date.microsecond
    return str(msec).zfill(6)

#returns array of months on checking if year is leap year ot not
def leapYearMonths(dateobj):
    months=[31,28,31,30,31,30,31,31,30,31,30,31]
    if dateobj.year%400==0 or dateobj.year%4==0 and dateobj.year%100!=0:
        months=[31,29,31,30,31,30,31,31,30,31,30,31]
    return months 

#returns day unumber of year
def getDays(dateobj):
    x=0
    months=leapYearMonths(dateobj)
    for i in range(dateobj.month-1):
        x+=months[i]
    return str(dateobj.day+x).zfill(3)

#returns week number of year ,where sunday is the start of the week.
def getWeeksU(dateobj):
    x=0
    months=leapYearMonths(dateobj)
    for i in range(dateobj.month-1):
        x+=months[i]
    return str(int((dateobj.day+x)/7)).zfill(2)

#returns week number of year ,where monday is the start of the week.
def getWeeksW(dateobj):
    x=0
    months=leapYearMonths(dateobj)
    for i in range(dateobj.month-1):
        x+=months[i]
    return str(int((dateobj.day+x)/7)).zfill(2)

#returns date in local format
def getLocalDate(dateobj):
    return str(dateobj.month).zfill(2)+"/"+str(dateobj.day).zfill(2)+"/"+str(dateobj.year)[2:5].zfill(2)

#returns time in local format
def getLocalTime(dateobj):
    return str(dateobj.hour).zfill(2)+":"+str(dateobj.minute).zfill(2)+":"+str(dateobj.second).zfill(2)



def str_f_time(dateobj,string):
    year,month,day=getDayMonthYear(dateobj)    #get year,month and day from date object
    code=string.replace(" ","").replace("\n","").replace("\t","")
    
    for i in range(0,len(code),2):
        if code[i:i+2] not in "%a%A%w%d%b%B%m%y%Y%H%I%p%M%S$f%j%U%W%c%x%X":  #Check if format code is wrong
            raise ValueError("Input From Code Format not present in [%a,%A,%W,%d,%b,%B,%m,%y,%Y,%H,%I,%p,%M,%S,$f,%j,%U,%W,%c,%x,%X]")

    if "%a" in string:
        string=string.replace("%a",getDay("%a",year,month,day))  #Short version of day

    if "%A" in string:
        string=string.replace("%A",getDay("%A",year,month,day)) #Full version of day

    if "%w" in string:
        string=string.replace("%w",getWeekDayNumber(year,month,day)) #Weekday as number (0 is Sunday)

    if "%d" in string:
        string=string.replace("%d",str(day))      #day Number

    if "%b" in string:
        string=string.replace("%b",getMonthName("%b",month)) #Short or Full version of month name

    if "%B" in string:
        string=string.replace("%B",getMonthName("%B",month)) #Short or Full version of month name

    if "%m" in string:
        if month<10:
            string=string.replace("%m","0"+str(month))
        else:
            string=string.replace("%m",str(month))

    if "%y" in string:
        string=string.replace("%y",getYear("%y",year))

    if "%Y" in string:
        string=string.replace("%Y",getYear("%Y",year))

    if "%H" in string:
        string=string.replace("%H",getCurrentHour24(dateobj))
    
    if "%I" in string:
        string=string.replace("%I",getCurrentHour12(dateobj))

    if "%p" in string:
        string=string.replace("%p",getAMorPM(dateobj))

    if "%M" in string:
        string=string.replace("%M",getCurrentMinute(dateobj))

    if "%S" in string:
        string=string.replace("%S",getCurrentSec(dateobj))

    if "$f" in string:
        string=string.replace("$f",getCurrentMicrosec(dateobj))

    if "%j" in string:
        string=string.replace("%j",getDays(dateobj))
   
    if "%U" in string:
        string=string.replace("%U",getWeeksU(dateobj))
        
    if "%W" in string:
        string=string.replace("%W",getWeeksW(dateobj))
    
    if "%c" in string:
        string=string.replace("%c",dateobj.ctime())
    
    if "%x" in string:
        string=string.replace("%x",getLocalDate(dateobj))
        
    if "%X" in string:
        string=string.replace("%X",getLocalTime(dateobj))
  
    return string



date=datetime.datetime(2018, 2, 8,10,22 ,21,100)

print(str_f_time(date,"%c"))
