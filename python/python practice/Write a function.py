#Write a function
#https://www.hackerrank.com/challenges/write-a-function
def is_leap(year):
    leap = False
    if year % 400 == 0:
        leap = True
    elif year % 4 == 0 and year % 100 != 0:
        leap = True
    # Write your logic here
    
    return leap
