import datetime

#get indivial date parameters
def dateinfo(dateobj,param):
    if str(dateobj)[20:26]=="":
        msec=0
    else:
        msec=int(str(dateobj)[20:26])
    switcher={
        "year":int(str(dateobj)[:4]),
        "month":int(str(dateobj)[5:7]),
        "day":int(str(dateobj)[8:11]),
        "hour":int(str(dateobj)[11:13]),
        "min":int(str(dateobj)[14:16]),
        "sec":int(str(dateobj)[17:19]),
        "msec":msec}
    return switcher.get(param,"invalid")

#calculates day of the week
def weekday(dateobj):
    y=dateinfo(dateobj,"year")
    m=dateinfo(dateobj,"month")
    d=dateinfo(dateobj,"day")
    t=[0,3,2,5,0,3,5,1,4,6,2,4]
    if m<3:
        y=y-1
    return int((y+y/4-y/100+y/400+t[m-1]+d)%7)

#converts date to timestamp(doesn't give exact value)
def totimestamp(dateobj):
    timestamp=0
    year=dateinfo(dateobj,"year")
    
    months=[31,28,31,30,31,30,31,31,30,31,30,31]
    if year%400==0 or year%4==0 and year%100!=0:
        months=[31,29,31,30,31,30,31,31,30,31,30,31]
        
    for i in range(1970,year):
        if i%400==0 or i%4==0 and i%100!=0:
            timestamp+=60*60*24*366
        else:
            timestamp+=60*60*24*365 
    for i in range(dateinfo(dateobj,"month")-1):
        timestamp+=months[i]*60*60*24
        
    timestamp+=dateinfo(dateobj,"day")*60*60*24
    return timestamp+dateinfo(dateobj,"hour")*60*60+dateinfo(dateobj,"min")*60+dateinfo(dateobj,"sec")+dateinfo(dateobj,"msec")/10**6

#converts timestamp to date return a datetime obj.(fetch value obtained in totimestamp() function)
def todate(timestamp):
    year=1970        
    days=timestamp/(24*60*60)
    
    rem=timestamp%(24*60*60) 
    hours=rem/(60*60)
    rem=rem%(60*60)
    minutes=rem/60
    rem=rem%60
    seconds=rem
    mseconds=round(rem%1,6)*10**6
    while int(days)>366 or int(days)>367:
        if year%400==0 or year%4==0 and year%100!=0:
            days-=366
            year+=1
        else:
            days-=365
            year+=1
            
    months=[31,28,31,30,31,30,31,31,30,31,30,31]
    if year%400==0 or year%4==0 and year%100!=0:
        months=[31,29,31,30,31,30,31,31,30,31,30,31]
    for j,d in enumerate(months):
        if int(days)>d:
            days-=d
        else:
            month=j+1
            break
    return datetime.datetime(year,month,int(days),int(hours),int(minutes),int(seconds),int(mseconds))

#returns date in utc time format
def to_utc(dateobj):
    year=dateinfo(dateobj,"year")
    month=dateinfo(dateobj,"month")
    day=dateinfo(dateobj,"day")
    hour=dateinfo(dateobj,"hour")-5
    minute=dateinfo(dateobj,"min")-30
    second=dateinfo(dateobj,"sec")
    msecond=dateinfo(dateobj,"msec")

    months=[31,28,31,30,31,30,31,31,30,31,30,31]
    if year%400==0 or year%4==0 and year%100!=0:
        months=[31,29,31,30,31,30,31,31,30,31,30,31]

    if minute<0:
        hour-=1
        minute+=60
    if hour<0:
        day-=1
        hour+=24
        print(hour)
    if day<1:
        month-=1
        day=months[month-1]
    if month<1:
        year-=1
        month+=12
    return datetime.datetime(year,month,day,hour,minute,second)

#returns normal date converted from utc date
def from_utc(dateobj):
    year=dateinfo(dateobj,"year")
    month=dateinfo(dateobj,"month")
    day=dateinfo(dateobj,"day")
    hour=dateinfo(dateobj,"hour")+5
    minute=dateinfo(dateobj,"min")+30
    second=dateinfo(dateobj,"sec")
    msecond=dateinfo(dateobj,"msec")
    
    months=[31,28,31,30,31,30,31,31,30,31,30,31]
    if year%400==0 or year%4==0 and year%100!=0:
        months=[31,29,31,30,31,30,31,31,30,31,30,31]
    
    if minute>60:
        hour+=1
        minute-=60
    if hour>24:
        day+=1
        hour-=24
    if day>months[month-1]:
        month+=1
        day=1
    if month>12:
        year+=1
        month-=12
    return datetime.datetime(year,month,day,hour,minute,second,msecond)

#returns formatted string
def c_time(dateobj):
    year=dateinfo(dateobj,"year")
    month=dateinfo(dateobj,"month")
    day=dateinfo(dateobj,"day")
    hour=dateinfo(dateobj,"hour")
    minute=dateinfo(dateobj,"min")
    second=dateinfo(dateobj,"sec")
    
    months={1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",7:"Jul",8:"Aug",9:"Sep",10:"Auc",11:"Nov",12:"Dec"}
    days={0:"Mon",1:"Tue",2:"Wed",3:"Thu",4:"Fri",5:"Sat",6:"Sun"}
    
    day_of_week=weekday(dateobj)
    return f"{days[day_of_week]} {months[month]}  {day} {str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(second).zfill(2)} {year}"

#adds time to date and returns a datetime object.
def addtime(dateobj,years=0,months=0,days=0,hours=0,minutes=0,seconds=0):
    year=dateinfo(dateobj,"year")+years
    month=dateinfo(dateobj,"month")+months
    day=dateinfo(dateobj,"day")+days
    hour=dateinfo(dateobj,"hour")+hours
    minute=dateinfo(dateobj,"min")+minutes
    second=dateinfo(dateobj,"sec")+seconds
    
    m=[31,28,31,30,31,30,31,31,30,31,30,31]
    if (year-years)%400==0 or (year-years)%4==0 and (year-years)%100!=0:
        m=[31,29,31,30,31,30,31,31,30,31,30,31]                
    while month>12 or day>m[(month-months-1)%12] or hour>=24 or minute>=60 or second>=60:
        minute+=int(second/60)
        second=second%60

        hour+=int(minute/60)
        minute=minute%60

        day+=int(hour/24)
        hour=hour%24
        
        if day>m[(month-months-1)%12]:
            day-=m[(month-months-1)%12]
            month+=1 
        
        year+=int(month/12)
        if month%12==0:
            month=12
            year-=1
        else:
            month=month%12
        if year%400==0 or year%4==0 and year%100!=0:
            m[1]=29
        else:
            m[1]=28
    return datetime.datetime(year,month,day,hour,minute,second)

#minuses time from date and returns a datetime object.
def removetime(dateobj,years=0,months=0,days=0,hours=0,minutes=0,seconds=0):
    year=dateinfo(dateobj,"year")
    month=dateinfo(dateobj,"month")

    m=[31,28,31,30,31,30,31,31,30,31,30,31]
    if (year-years)%400==0 or (year-years)%4==0 and (year-years)%100!=0:
        m=[31,29,31,30,31,30,31,31,30,31,30,31] 
    totalsec=totimestamp(dateobj)
    if seconds!=0:
        totalsec-=seconds
    if minutes!=0:
        totalsec-=minutes*60
    if hours!=0:
        totalsec-=hours*60*60
    if days!=0:
        totalsec-=days*24*60*60
    if months!=0:
        for i in range(1,months+1):
            totalsec-=m[(month-i)%12]*24*60*60
    if years!=0:
        for i in range(1,years+1):
            if (year-i)%400==0 or (year-i)%4==0 and (year-i)%100!=0:
                totalsec-=60*60*24*366
            else:
                totalsec-=60*60*24*365
    date_tuple=todate(totalsec)
    
    return todate(totalsec)


#all functions here accepts datetime or date object as dateobj parameter
y=datetime.datetime(2020,11,11,11,11)

print("\nyear:",dateinfo(y,"year"),"\n")
print("day of week:",weekday(y),"\n")
print("to timestamp:",totimestamp(y),"\n")
print("to date:",todate(1607771460.0),"\n")
print("to UTC:",to_utc(y),"\n")
print("from UTC:",from_utc(y),"\n")
print("formatted date:",c_time(y),"\n")
print("time added date:",addtime(y,days=20,years=10),"\n")
print("time removed date:",removetime(y,days=11,hours=1))