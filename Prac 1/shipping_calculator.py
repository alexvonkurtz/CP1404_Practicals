"""
A  shipping  company  requires  a  small  program  that  would  allow  them  to  quickly  work  out  total  shipping  
charge   for  a  number  of  items,  each  with  different  prices.   The  program  allows  the  user  to  enter  the  
number  of  items  and  the  shipping  cost  for  each  different  item.     Then  the  program  computes  and  displays  
the  total  shipping  cost.   If  the  total  shipping  cost  is  over  $100,  then  a  10%  discount  is  applied  to
the  total  shipping  cost  before  the   amount  is  displayed  on  the  screen.  

The  output  might  look  something like:  

Number  of  items:  3  
Price  of  item:  100  
Price  of  item:  21.56  
Price  of  item:  3  
Total  price  for  3  items  is  $112.10  

Note:  start  with  the  main  logic,  then  adjust  your  program  to  improve  the  formatting.    

+  Error  checking  (input  validation  loop):  If  the  number  of  items  is  less  than  zero,  
a  message  should  be   displayed  (e.g.  “Invalid  number  of  items!”)  and  this  quantity  must  
be  re-­entered  by  the  user  until  it  is  valid.
"""

__author__ = 'Alex Von Kurtz'

items = []
item = (int(input("How many items are there? ")))
total_item = item
while item > 0:
    item = item - 1
    item_Price = (float(input("What is the price of the item?: ")))
    items.append(item_Price)
total = sum(items)
discount = 0
if total > 100:
    discount = total * 0.10
    overall_total = total - discount
else:
    overall_total = sum(items)
print ("Total price for",total_item,"items is","${:.2f}".format(overall_total))
