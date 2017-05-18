

import calendar

age= int(input("age:"))
date= int(input("Date of Birth:"))
month=int(input("month of Birth:"))
current_year = int(input("current year:"))
year_of_birth = current_year-age

day_of_birth = calendar.weekday(year_of_birth,month,date)
day_string = calendar.day_name[day_of_birth]

print("YOU WERE BORN ON A" + day_string +"in" +str(year_of_birth))
      


          

