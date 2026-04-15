#leap year
def leap_year(n):
    if (n%4==0 or n%400==0):
        print(n,"is leap year")
    else:
        print(n,"is not a leap year")
leap_year(2024)