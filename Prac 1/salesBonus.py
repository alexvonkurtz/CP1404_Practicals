"""
Program  to  calculate
and  display
a  user's  bonus  based  on  sales.
If  sales  are  under  $1,000,  the  user  gets  a  10%  bonus.
If  sales  are  $1,000  or  over,  the  bonus  is  15%.
"""
__author__ = 'Alex Von Kurtz'

print("Please enter your sales")
sales  =  float(input("Enter  sales:  $"))
while sales > 0:
    if sales < 1000:
        print ("Your sale is less than $1000 you receive a 10% bonus")
        total = sales * 0.10
    else:
         print("Your sale is greater than $1000 you receive a 15% bonus")
         total = sales * 0.15
    print(total)
    sales = float(input("Enter  sales:  $"))
