year = 2024

if (year % 400 == 0) | (year % 4 == 0 and year % 100 != 0):
    status = str(year) + " is leap year."
else:
   status = str(year) + " is not a leap year"

print(status)