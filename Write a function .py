def is_leap(year):
    if(year == 1800 or year == 1900 or year == 2100 or year ==2200 or year == 2300 or year==2500):
        return False
    elif(year%4 == 0):
        return True
    elif(year%100 != 0):
        return False
    elif(year%400 == 0):
        return True

year = int(input())
print (is_leap(year))