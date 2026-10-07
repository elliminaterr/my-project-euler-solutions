WEEK = 7
YEAR = 12
CENTURY = 100
months = [31,28,31,30,31,30,31,31,30,31,30,31]
leap_year_months = [31,29,31,30,31,30,31,31,30,31,30,31]
day = 1
date = 1
counter = 0
for i in range(1,CENTURY+1):
    leap_year = False
    if i % 4 == 0:
        leap_year = True
    for j in range(YEAR):
        if leap_year:
            current_month = leap_year_months[j]
        else:
            current_month = months[j]
        date = 0
        for k in range(current_month):
            if date == 1 and day == 0:
                counter += 1
            day = (day + 1) % 7
            date += 1
print(counter)
