"""
1.   When  will  a  ValueError  occur?

When a decimal number is inputted

2.   When  will  a  ZeroDivisionError  occur?

when the single number zero is entered in the denominator

3.      Could  you  change  the  code  to  avoid  the  possibility  of  a  ZeroDivisionError?

No, you could only warn the user that dividing by zero cannot occur. We cannot determine the users input
therefore the ZeroDivisionError is required as a warning.

"""

try:
    numerator  =  int(input("Enter the numerator:  "))
    denominator  =  int(input("Enter the denominator:  "))
    fraction  =  numerator/denominator
except ValueError:
    print("Numerator  and  denominator  must  be  valid  numbers!")
except ZeroDivisionError:
    print("Cannot  divide  by  zero!")
print("Finished.")

