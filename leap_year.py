def is_year_leap(year):
    if (year % 400 == 0) and (year % 100 == 0):
        print("{0} is a leap year".format(year))

    elif (year % 4 ==0) and (year % 100 != 0):
        print("{0} is a leap year".format(year))

    else:
        print("{0} is not a leap year".format(year))

def days_in_month(year, month):
    
    if((month==2) and ((year%4==0)  or ((year%100==0) and (year%400==0)))) :
        print("Number of days is 29")
 
    elif(month==2) :
        print("Number of days is 28")
 
    elif(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) :
        print("Number of days is 31")
 
    else :
        print("Number of days is 30")

month = int(input('Enter a month number '))
year = int(input('Enter a year '))
is_year_leap(year)
days_in_month(year, month)
