x = 5
if x < 10:
    print('Smaller')
if x < 8:
    print('Bigger')
print('Finish')
print(int(98.6))

astr = 'BOB'
try:
    print('Hello')
    istr = int(astr)
    print('There')
except:
    istr = -1

print('Done', istr)

#Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input - assume the user types numbers properly.

'''
hrs = input("Enter Hours:")
rate = float(input("Enter Rate:"))
h = float(hrs)
if h <= 40:
    rate_per_hour = h * rate
    print(rate_per_hour)
else:
    extra_hours = h - 40
    cost_extra_hours = (extra_hours * rate) * 1.5
    print(cost_extra_hours)
    rate_per_hour = (40*rate) + cost_extra_hours
    print(rate_per_hour)


sh = input("Enter Hours:")
sr = input("Enter Rate:")

try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input")
    quit()
print(fh, fr)
if fh > 40:
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh *fr
print("Pay:", xp)
'''

'''3.3 Write a program to prompt for a score between 0.0 and 1.0.
If the score is out of range, print an error. If the score is between 0.0 and 1.0,
print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit.
For the test, enter a score of 0.85.'''


try:
    score = float(input("Enter Score: "))
    if score <= 1.0 and score >= 0.0:
        if score >= 0.9:
            print("A")
        elif score >= 0.8:
            print("B")
        elif score >= 0.7:
            print("C")
        elif score >= 0.6:
            print("D")
        else:
            print("F")
except:
    print("Error, the score is not between 0.0 and 1.0")
    quit()
