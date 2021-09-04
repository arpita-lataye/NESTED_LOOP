# to get next day of a given date

year=int(input("input a year:"))
if year%400==0:
    print("leap year")
elif year%100:
    print("no leap year")
elif year%4==0:
    print("leap year")
else:
    print("no leap year")
month=int(input("enter month 1 to 12 :"))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print("31 days in this month")
elif month==2:
    print("28 or 29 days in this month")
else:
    print("30 days in this month")
day=int(input("enter day 1 to 31:"))
if day<month:
    day=day+1
else:
    day=1
    if month==12:
        month=1
        year=year+1
    else:
        month=month+1
print("the next date is (yyyy-mm-dd)"%(year,month,day))
