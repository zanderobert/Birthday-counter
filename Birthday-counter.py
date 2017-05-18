import calendar
age = int(input ('Age'))
month = int (input('Month of birth (1-12):'))
Date = int (input ('Date of birth (1-32):'))
Current_year = int (input ('Current Year:'))
year = Current_year - age
day = calendar.weekday(year, month, Date)
day_string = calendar.day_name[day]
print ('you were born on a ' + day_string + ' in the year '  + str (year))
